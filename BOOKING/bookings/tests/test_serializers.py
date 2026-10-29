from django.test import TestCase
from django.contrib.auth import get_user_model

from bookings.serializers import BookingCreateSerializer, BookingListSerializer, BookingDetailListSerializers
from listing.models import HostProfile, Category, Space
from bookings.models import Booking, BookingStatus


User = get_user_model()


class BookingCreateSerializerTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            phone="09123456789",
            email="host@example.com",
            first_name="Test",
            last_name="Host",
            password="testpassword123",
        )

        self.host = HostProfile.objects.create(
            user=self.user,
            name="Test Host",
            bio="Test host bio",
        )

        self.category = Category.objects.create(
            name="Meeting Room",
            slug="meeting-room",
            description="A room for meetings",
        )

        self.space = Space.objects.create(
            host=self.host,
            category=self.category,
            title="Test Space",
            description="A space for testing",
            price=100,
            city="Berlin",
            address="Test Address",
        )

    def test_book_create_serializer_valid_data(self):
        serializer = BookingCreateSerializer(
            data={
                "space": self.space.pk,
                "start_at": "2026-11-01T10:00:00Z",
                "end_at": "2026-11-01T12:00:00Z",
            }
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_invalid_space(self):
        serializer = BookingCreateSerializer(
            data={
                "space": 999999,
                "start_at": "2026-11-01T10:00:00Z",
                "end_at": "2026-11-01T12:00:00Z",
            }
        )

        self.assertFalse(serializer.is_valid())
        self.assertIn("space", serializer.errors)

    def test_missing_space(self):
        serializer = BookingCreateSerializer(
            data={
                "start_at": "2026-11-01T10:00:00Z",
                "end_at": "2026-11-01T12:00:00Z",
            }
        )

        self.assertFalse(serializer.is_valid())
        self.assertIn("space", serializer.errors)


    def test_book_list_serializer(self):
        booking = Booking.objects.create(
            space=self.space,
            user=self.user,
            price=100,
            start_at='2026-11-01T10:00:00Z',
            end_at='2026-11-01T12:00:00Z'
        )

        

        serializer = BookingListSerializer(instance=booking)

        self.assertEqual(serializer.data['price'], 100)
        self.assertIn('status', serializer.data)
        self.assertEqual(serializer.data['space'], self.space.pk)
        self.assertGreaterEqual(serializer.data['price'], 0)
        self.assertNotIn('user', serializer.data)



    def test_book_detail_serializer(self):
        booking = Booking.objects.create(
            space=self.space,
            user=self.user,
            price=100,
            start_at='2026-11-01T10:00:00Z',
            end_at='2026-11-01T12:00:00Z',
        )

        serializer = BookingDetailListSerializers(instance=booking)

        self.assertEqual(serializer.data['status'], BookingStatus.PENDING)
        self.assertEqual(serializer.data['space'], self.space.pk)
        self.assertEqual(serializer.data['user'], self.user.pk)
        self.assertGreaterEqual(serializer.data['price'], 0)
        self.assertEqual(serializer.data['price'], 100)
        self.assertEqual(serializer.data['start_at'], '2026-11-01T10:00:00Z')
        self.assertEqual(serializer.data['end_at'], '2026-11-01T12:00:00Z')




