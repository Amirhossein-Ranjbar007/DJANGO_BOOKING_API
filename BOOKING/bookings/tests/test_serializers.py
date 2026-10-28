from django.test import TestCase
from django.contrib.auth import get_user_model

from bookings.serializers import BookingCreateSerializer
from listing.models import HostProfile, Category, Space


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

    def test_valid_data(self):
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