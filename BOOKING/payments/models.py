from django.db import models
from users.models import User
from bookings.models import Booking
import uuid


class PaymentsStatus(models.TextChoices):

    SUCCESSFUL = 'Successful', 'successful'
    FAILURE = 'Failure', 'failure'
    PENDING = 'Pending', 'pending'
    CANCELED = 'Cancel', 'cancel'



class Payments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pay')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking_pay')
    authority = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    status = models.CharField(max_length=15, choices=PaymentsStatus, default=PaymentsStatus.PENDING)
    amount = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking} - {self.user}"


class PaymentTransactionStatus(models.TextChoices):

    SUCCESSFUL = 'Successful', 'successful'
    FAILURE = 'Failure', 'failure'
    PENDING = 'Pending', 'pending'


class PaymentTransaction(models.Model):

    payments = models.ForeignKey(Payments, on_delete=models.CASCADE, related_name='transaction')
    status = models.CharField(max_length=15, choices=PaymentTransactionStatus, default=PaymentTransactionStatus.PENDING)
    reference_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


class MockPaymentSessionStatus(models.TextChoices):

    SUCCESSFUL = 'Successful', 'successful'
    PENDING = 'Pending', 'pending'
    FAILED = 'Failed', 'failed'
    EXPIRED = 'Expired', 'expired'


class MockPaymentSession(models.Model):

    payments = models.ForeignKey(Payments, on_delete=models.CASCADE, related_name='mock')
    authority = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    status = models.CharField(max_length=15, choices=MockPaymentSessionStatus, default=MockPaymentSessionStatus.PENDING)
    start_time = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()











