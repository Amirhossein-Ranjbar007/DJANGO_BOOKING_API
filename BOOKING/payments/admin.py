from django.contrib import admin
from .models import Payments,PaymentTransaction


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):

    list_display = ['booking', 'status', 'amount', 'created_at']
    search_fields = ['booking']
    list_filter = ['booking']



@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):

    list_display = ['payments_booking', 'payments_user', 'status']
    list_select_related = ['payments_booking', 'payments_user']
    readonly_fields = ['booking_display', 'user_display']

    def payments_booking(self, obj):
        return obj.payments.booking
    payments_booking.short_description = 'booking'

    def payments_user(self, obj):
        return obj.payments.user
    payments_user.short_description = 'user'

    def booking_display(self, obj):
        return obj.payments.booking
    booking_display.short_description = 'booking'

    def user_display(self, obj):
        return obj.payments.user
    user_display.short_description = 'user'



