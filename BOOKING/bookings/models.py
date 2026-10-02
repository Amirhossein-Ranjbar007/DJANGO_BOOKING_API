from django.db import models
from listing.models import Space
from users.models import User
from django.db.models import Q,F


class BookingSchedule(models.Model):

    space = models.OneToOneField(Space, on_delete=models.CASCADE, related_name='space_sched')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ScheduleDay(models.Model):

    schedule = models.ForeignKey(BookingSchedule, on_delete=models.CASCADE, related_name='schedule')
    weekday = models.PositiveIntegerField()
    start_at = models.TimeField()
    end_at = models.TimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition= (models.Q(weekday__gte=0) & models.Q(weekday__lte=6)
                ),
            name='weekday_ambit'
            ),
            models.CheckConstraint(
                condition= (
                    models.Q(start_at__lt=F('end_at'))
                ),
                name='duration_ambit'
            ),
            models.UniqueConstraint(
                fields=['schedule', 'weekday'],
                name='unique_schedule_weekday',
            ),
        ]



class BookingSlot(models.Model):

    day = models.ForeignKey(ScheduleDay, on_delete=models.CASCADE, related_name='slot')
    start_time = models.TimeField()
    end_time = models.TimeField()


    class Meta:
        constraints = [
            models.CheckConstraint(
                condition= models.Q(start_time__lt=F('end_time')),
                name='slot_duration_ambit',
            )
        ]



class BookingStatus(models.TextChoices):

    CONFIRMED = 'confirmed', 'Confirmed'
    PENDING = 'pending', 'Pending'
    CANCELED = 'canceled', 'Canceled'
    COMPLETED = 'completed', 'Completed'



class Booking(models.Model):

    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='spacebook')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(max_length=10, choices=BookingStatus.choices, default=BookingStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition= models.Q(start_at__lt=F('end_at')),
                name='booking_duration_ambit',
            )
        ]




















