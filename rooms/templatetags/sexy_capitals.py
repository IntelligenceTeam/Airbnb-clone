from django import template

register = template.Library()


@register.filter  # filter()안에 이름을 이 파일이름과 동일하게 한다.
def sexy_capitals(value):  # 함수 이름을 다른 걸 쓰고 싶으면
    print(value)
    return value.capitalize()
