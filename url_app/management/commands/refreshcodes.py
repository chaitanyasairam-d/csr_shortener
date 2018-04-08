from django.core.management.base import BaseCommand, CommandError
from url_app.models import UrlShortener

class Command(BaseCommand):
    help = 'Refreshes All Short Codes'

    def add_arguments(self,parser):
        parser.add_argument('items',type=int)


    def handle(self, *args, **options):
        print(options)
        return UrlShortener.objects.refresh_shortcodes(items=options['items'])
