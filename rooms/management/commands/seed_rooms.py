import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = (
            user_models.User.objects.all()
        )  # 원래라면 all()은 하지 않는게 좋다. 모든 정보를 가져올 필요는 없다.
        room_types = (
            room_models.RoomType.objects.all()
        )  # 만약 저장된 정보가 20000개 이상이면 상당히 불필요하게 시간을 낭비하는 것.
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),  # 가짜 stuff(정보라고 해도 될 듯)를 만드는데 최적화된 라이브러리 faker를 사용
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
