from django.core.management.base import BaseCommand, CommandError
from shortner.models import Krikurl

class Command(BaseCommand):
    help = 'refreshes all shortcodes'

    

    def handle(self, *args, **options):
        return Krikurl.objects.refresh_shortcodes()
        