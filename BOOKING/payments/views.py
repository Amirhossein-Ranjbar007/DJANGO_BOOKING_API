from django.shortcuts import render
from rest_framework.views import APIView
from .models import Payments, PaymentTransaction
from .serializers import PaymentCreateSerializer,PaymentListSerializer
from rest_framework import status
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.permissions import IsAuthenticated
from .services import create_payment, create_mockpay_session
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PaymentsListPagination
from .filters import PaymentListFilter
from django.db import transaction
from rest_framework.exceptions import PermissionDenied
from .mockpay import get_session, execute_payment
from rest_framework.exceptions import ValidationError
from django.conf import settings




class PaymentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @transaction.atomic
    def post(self, request):

        serializer = PaymentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment = create_payment(user=request.user, booking=serializer.validated_data['booking'])

        session = create_mockpay_session(payment=payment)

        response = {'id': payment.id, 'authority': str(payment.authority), 'amount': payment.amount,
                    'status': payment.status, 'session_authority': str(session.authority), 'gateway_url': f'/api/mockpay/{session.authority}/',
                    'expires_at': session.expires_at,}

        return Response(response, status=status.HTTP_201_CREATED)


class PaymentListView(ListAPIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    serializer_class = PaymentListSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['booking__space__title']

    ordering_fields = ['amount', 'created_at']
    ordering = ['created_at']

    pagination_class = PaymentsListPagination
    filterset_class = PaymentListFilter

    def get_queryset(self):
        user = self.request.user
        return Payments.objects.filter(user=user)



class MockPaySessionView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, authority):
        session = get_session(authority)

        if session.payments.user_id != request.user.id:
            raise PermissionDenied(
                'You do not have permission to access this payment session.'
            )

        response = {
            'session_authority': str(session.authority),
            'session_status': session.status,
            'payment_id': session.payments_id,
            'amount': session.payments.amount,
            'expires_at': session.expires_at,
        }

        return Response(response, status=status.HTTP_200_OK)


class MockpayExecuteView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request, authority):

        """Simulates a payment gateway response for demonstration purposes.
        In production, the result must be verified through a real payment gateway API.
        """

        if not settings.DEBUG:
            raise PermissionDenied('Mock payment is only available in debug mode.')

        result = request.data.get('result')
        if result in ['success', 'failure']:

            session = get_session(authority)

            if request.user.id != session.payments.user_id:
                raise ValidationError('ids are not match!')

            successful = (result == 'success')

            exe = execute_payment(session=session, successful=successful)
            session.refresh_from_db()

            return Response({'payment_id': exe.id, 'payment_status': exe.status, 'session_status': session.status,}, status=status.HTTP_200_OK)






