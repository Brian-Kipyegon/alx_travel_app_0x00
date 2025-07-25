from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Listing, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]
        read_only_fields = ["id"]


class BookingSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["id", "guest", "created_at", "updated_at"]


class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = "__all__"
        read_only_fields = ["id", "host", "created_at", "updated_at"]
