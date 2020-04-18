from django.shortcuts import render
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", 1))  # str타입이기 때문에 int형변환을 해줘야 한다.
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={"rooms": all_rooms})

    """
        limit - 페이지 제한 수, 몇 개의 페이지를 보여줄 것인가
        offset - 시작 페이지를 계산하기 위함. 1~10페이지까지 보여준다 할 때 시작페이지인 1을 가리키는 인덱스.

    """
