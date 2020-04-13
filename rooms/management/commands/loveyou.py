from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))

    """
        print(args, options)를 해보면 
        () {'verbosity': 1, 'settings': None, 'pythonpath': None, 'traceback': False, 'no_color': False, 
        'force_color': False, 'times': '50'}
        이 나오고 options.get("times")를 하면 '50'은 string이 때문에
        for문에서는 int형변환을 해야 한다.

        그리고 원래대로 라면 self.stdout.write부분에서
        안에 SUCCESS를 하면 초록색 메시지,
        ERROR를 하면 빨간색, 
        WARNING을 하면 주황색 메시지가 뜨는데 (맥에서는 그렇게 나오는 듯)
        윈도우 10에서는 그렇게 나오지 않는거 같다. 

        이 부분은 Basecommand 부분에서 ctrl + 클릭한 것을 통해 강의에서 써본 것 같다.
    """
