from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
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

    accuracy = forms.ChoiceField(choices=VALUE_CHOICE)  # 이렇게 1에서 5를 선택해서 하는 방법도 있음
    communication = forms.IntegerField(max_value=5, min_value=1)
    cleanliness = forms.IntegerField(max_value=5, min_value=1)
    location = forms.IntegerField(max_value=5, min_value=1)
    check_in = forms.IntegerField(max_value=5, min_value=1)
    value = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleanliness",
            "location",
            "check_in",
            "value",
        )

    def save(self):
        review = super().save(commit=False)
        return review
