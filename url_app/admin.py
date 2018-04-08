from django.contrib import admin
from url_app.models import UrlShortener #from .models import UrlShortner
# Register your models here.
admin.site.register(UrlShortener)
