from .models import (Payments, PaymentTransaction,PaymentsStatus,PaymentTransactionStatus,
                     MockPaymentSession, MockPaymentSessionStatus)
from rest_framework.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone
import datetime



@transaction.atomic
def create_payment(*, user, booking):

    if user.id != booking.user.id:
        raise ValidationError('this reservation is not yours!')

    if Payments.objects.filter(booking=booking, status=PaymentsStatus.SUCCESSFUL).exists():
        raise ValidationError(f"this booking has already paid!")

    pending_payment = Payments.objects.filter(
        booking=booking,
        user=user,
        status=PaymentsStatus.PENDING
    ).first()

    if pending_payment:
        return pending_payment

    payment = Payments.objects.create(user=user, booking=booking, amount=booking.price, status=PaymentsStatus.PENDING)

    PaymentTransaction.objects.create(payments=payment, status=PaymentTransactionStatus.PENDING)

    return payment



@transaction.atomic
def create_mockpay_session(*, payment):

    if payment.status != PaymentsStatus.PENDING:
        raise ValidationError(f'this payment is not in pending status!')

    expired_at = timezone.now() + datetime.timedelta(minutes=10)

    session = MockPaymentSession.objects.create(payments=payment, status=MockPaymentSessionStatus.PENDING,
                                                expires_at=expired_at)

    return session





