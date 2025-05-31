from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing, related_name="bookings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} booking for {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(
        Listing, related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.listing.title}"
