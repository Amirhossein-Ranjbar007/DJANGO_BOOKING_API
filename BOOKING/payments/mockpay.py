from .models import MockPaymentSession, MockPaymentSessionStatus, Payments, PaymentTransactionStatus, PaymentsStatus
from rest_framework.exceptions import NotFound ,ValidationError
from django.utils import timezone
from django.db import transaction

def get_session(authority):
    try:
        session = (
            MockPaymentSession.objects.select_related('payments').get(authority=authority)
        )
    except MockPaymentSession.DoesNotExist:
        raise NotFound('Payment session not found.')

    if session.status == MockPaymentSessionStatus.EXPIRED:
        raise ValidationError('This payment session has expired.')

    if session.expires_at <= timezone.now():
        if session.status == MockPaymentSessionStatus.PENDING:
            session.status = MockPaymentSessionStatus.EXPIRED
            session.save(update_fields=['status'])

        raise ValidationError('This payment session has expired.')

    return session

@transaction.atomic
def execute_payment(*, session, successful):

    """Simulates payment execution for demonstration purposes.
    In production, integrate a real payment gateway and verify results server-side.
    """

    session = (
        MockPaymentSession.objects
        .select_for_update()
        .select_related('payments')
        .get(pk=session.pk)
    )

    payment = session.payments

    if session.status != MockPaymentSessionStatus.PENDING:
        raise ValidationError('This session has already been processed.')

    if session.expires_at <= timezone.now():
        session.status = MockPaymentSessionStatus.EXPIRED
        session.save(update_fields=['status'])
        raise ValidationError('This payment session has expired.')

    if payment.status != PaymentsStatus.PENDING:
        raise ValidationError('This payment cannot be processed.')

    payment_transaction = (
        payment.transaction
        .select_for_update()
        .order_by('-created_at')
        .first()
    )

    if payment_transaction is None:
        raise ValidationError('Payment transaction not found.')

    if successful:
        session.status = MockPaymentSessionStatus.SUCCESSFUL
        payment.status = PaymentsStatus.SUCCESSFUL
        payment_transaction.status = PaymentTransactionStatus.SUCCESSFUL
    else:
        session.status = MockPaymentSessionStatus.FAILED
        payment.status = PaymentsStatus.FAILURE
        payment_transaction.status = PaymentTransactionStatus.FAILURE

    session.save(update_fields=['status'])
    payment.save(update_fields=['status', 'updated_at'])
    payment_transaction.save(update_fields=['status'])

    return payment


def expire_session(session):
    if session.status != MockPaymentSessionStatus.PENDING:
        raise ValidationError(
            'Only pending sessions can be expired.'
        )

    if session.expires_at > timezone.now():
        raise ValidationError(
            'This session has not expired yet.'
        )

    session.status = MockPaymentSessionStatus.EXPIRED
    session.save(update_fields=['status'])

    return session


