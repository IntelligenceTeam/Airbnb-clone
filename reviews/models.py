from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    VALUE_ONE = 1
    VALUE_TWO = 2
    VALUE_THREE = 3
    VALUE_FOUR = 4
    VALUE_FIVE = 5

    VALUE_CHOICE = (
        (VALUE_ONE, "1"),
        (VALUE_TWO, "2"),
        (VALUE_THREE, "3"),
        (VALUE_FOUR, "4"),
        (VALUE_FIVE, "5"),
    )

    review = models.TextField()
    accuracy = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], choices=VALUE_CHOICE
    )
    communication = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], choices=VALUE_CHOICE
    )
    cleanliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], choices=VALUE_CHOICE
    )
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], choices=VALUE_CHOICE
    )
    check_in = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], choices=VALUE_CHOICE
    )
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], choices=VALUE_CHOICE
    )
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."

    class Meta:
        ordering = ("-created",)  # ordering은 반드시 튜플로 만들어야 함.
