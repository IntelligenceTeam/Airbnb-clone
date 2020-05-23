import datetime
from django.db import models
from django.utils import timezone
from core import models as core_models


class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        #  4815 Foster Stream Suite 731 North Wyatt, SD 49976 - 2020-04-17을 눌렀을 때
        if True:  # 이미 만들어진 거로 테스트하려면 True로 해야 됨
            start = self.check_in
            print(start)  # 2020-04-17
            end = self.check_out
            print(end)  # 2020-04-26
            difference = end - start
            print(difference)  # 9 days, 0:00:00
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()
            print(existing_booked_day)  # False
            if not existing_booked_day:
                super().save(*args, **kwargs)
                print(difference.days + 1)  # 10
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    print(day)
                    # 2020-04-17 2020-04-18 2020-04-19 2020-04-20
                    # 2020-04-21 2020-04-22 2020-04-23 2020-04-24 2020-04-25 2020-04-26
                    BookedDay.objects.create(day=day, reservation=self)

        return super().save(*args, **kwargs)
