from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "displays current time"

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime("%X")
        self.stdout.write("its now %s" % time)
