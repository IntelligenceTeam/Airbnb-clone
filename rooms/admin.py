from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules"),},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")
    # 도시 이름이 같거나, 호스트의 이름 첫 시작이 같으면 검색됨.

    filter_horizontal = ("amenities", "facilities", "house_rules")
    # ManyToMany Field에 적용 가능.

    def count_amenities(self, obj):  # list_display에 함수를 쓰고 싶을 때는 이름을 동일하게 써준다.
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        print(obj)  # Very Nice Place
        print(type(obj))  # <class 'rooms.models.Photo'>
        print(obj.file)  # 집2.jpg
        print(type(obj.file))  # <class 'django.db.models.fields.files.ImageFieldFile'>

        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')
        # 장고는 보안상 입력값으로부터 html이든 자바스크립트 코드든 아무거나 함부로 나타나지 않게 한다.
        # 위의 이미지 태그도 mark_safe 없이 그냥 써버리면 저 html로 그대로 나오고 사진은 나오지 않는다.
        # 이를 이미지 태그로 적용되어 사진으로 표현하기 위해서 mark_safe를 사용하는 것이다.
        # mark_safe는 무분별한 입력값들을 분별하기 위해서 장고에 이 입력값은 괜찮다는 것을 알려주는 라이브러리다.

    get_thumbnail.short_description = "Thumbnail"
