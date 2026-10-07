from .models import Booking,BookingSlot,BookingSchedule,ScheduleDay
from listing.models import Space, SpaceStatus
from rest_framework.exceptions import ValidationError
from django.db import transaction
from django.core.cache import cache
import time

@ transaction.atomic
def create_booking(*, user, space, start_at, end_at):

    if space.status != SpaceStatus.ACTIVE:
        raise ValidationError('this space is not active!')

    try:
        schedule = space.space_sched
    except BookingSchedule.DoesNotExist:
        raise ValidationError('this space has no booking schedule!')

    if not schedule.is_active:
        raise ValidationError('this space schedule is not active!')


    day_num = start_at.weekday()

    try:
        schedule_weekday = ScheduleDay.objects.get(schedule=schedule, weekday=day_num)

    except ScheduleDay.DoesNotExist:
        raise ValidationError('no activity is possible in this day!')

    start_at_time = start_at.time()
    end_at_time = end_at.time()
    schedule_duration = ScheduleDay.objects.filter(schedule=schedule, weekday = day_num, start_at__lte=start_at_time, end_at__gte=end_at_time)
    if schedule_duration.exists() == False:
        raise ValidationError('invalid input/ start an end time must be in determinate ambit!')


    slot = BookingSlot.objects.get(day=schedule_weekday, start_time=start_at_time)

    while slot.end_time != end_at_time:

        if slot.end_time > end_at_time:
            raise ValidationError('Invalid ambit!/ You can\'t choose this endtime!')

        try:
            next_slot = BookingSlot.objects.get(day=schedule_weekday, start_time=slot.end_time)
        except BookingSlot.DoesNotExist:
            raise ValidationError('ERROR!')

        slot = next_slot

    booking = Booking.objects.filter(space=space, start_at__lt=end_at, end_at__gt=start_at)
    if booking.exists():
        raise ValidationError('You can\'t choose this time!')


    duration = end_at - start_at

    if space.price_unit == 'day':
        total_price = space.price * (duration.total_seconds()/86400)
    if space.price_unit == 'hour':
        total_price = space.price * (duration.total_seconds()/3600)

    booking = Booking.objects.create(user=user, space=space, price=total_price, start_at=start_at, end_at=end_at )

    return booking


@transaction.atomic
def booking_cancelation(booking):

    if booking.status in ['completed', 'canceled']:
        raise ValidationError("you can only cancel bookings that they are only in confirmed and pending level")

    if booking.status in ['confirmed', 'pending']:
        booking.status = 'canceled'

    booking.save()

    cache_key = f"BookingDetail:{booking.id}:{booking.user_id}"
    cache.delete(cache_key)

    list_timestamp_key = f'booking_ts_{booking.user_id}'
    cache.set(list_timestamp_key, time.time())

    return booking













