from django.db.models import Q
from django.shortcuts import render
from users import models as user_models
from . import models


def go_conversation(request, a_pk, b_pk):
    user_one = user_models.User.objects.get_or_none(pk=a_pk)
    user_two = user_models.User.objects.get_or_none(pk=b_pk)
    if user_one is not None and user_two is not None:
        conversation = models.Conversation.objects.get(
            Q(participants=user_one) & Q(participants=user_two)
        )
        print(conversation)
        # part 1, get_or_none은 사용이 안된다. 인자가 하나만 있어야 한다.
        # TypeError at /conversations/go/37/1
        #  get_or_none() takes 1 positional argument but 2 were given
