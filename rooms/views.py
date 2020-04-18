from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

    # class based view 식으로 할 때는 render할 파일명이 애플리케이션 이름과 동일시하거나 오류가 날 때 알려준다
