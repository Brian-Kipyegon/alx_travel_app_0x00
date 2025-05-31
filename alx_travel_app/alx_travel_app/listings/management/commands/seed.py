from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Cozy Cottage",
                "description": "A beautiful cottage in the countryside.",
                "location": "Nairobi",
                "price_per_night": 100.00,
                "available": True,
            },
            {
                "title": "Luxury Villa",
                "description": "Experience luxury like never before.",
                "location": "Mombasa",
                "price_per_night": 250.00,
                "available": True,
            },
            {
                "title": "Beachside Bungalow",
                "description": "Relax by the beach with this stunning bungalow.",
                "location": "Diani",
                "price_per_night": 180.00,
                "available": True,
            },
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created listing: {listing.title}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Listing already exists: {listing.title}")
                )

        # Optionally, create a test user for bookings and reviews
        if not User.objects.filter(username="testuser").exists():
            User.objects.create_user(username="testuser", password="password123")
            self.stdout.write(self.style.SUCCESS("Created test user: testuser"))
