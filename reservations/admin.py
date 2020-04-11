from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status", "in_progress")
    """
        위에 in_progress를 추가하니까 나오는 에러. 수정은 이후 챕터에서 수행.
        ERRORS:
        <class 'reservations.admin.ReservationAdmin'>: (admin.E116) The value of 'list_filter[1]' refers to 'in_progress', which does not refer to a Field.
    """
