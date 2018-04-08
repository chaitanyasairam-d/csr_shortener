from django.conf import settings
from django.db import models
from .utils import create_shortcode,code_generator
# Create your models here.

SHORTCODE_MAX = settings.SHORTCODE_MAX
class UrlShortenerManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(UrlShortenerManager, self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self,items=1):
        qs = UrlShortener.objects.filter(id__gte=1)
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(self)
            q.save()
            new_code += 1
            print(q.shortcode)
        return "New_Codes Made: {i}".format(i=new_code)
class UrlShortener(models.Model):
    url = models.URLField(max_length=300)
    shortcode = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    active = models.BooleanField(default=True)
    objects = UrlShortenerManager()

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        return super(UrlShortener,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)
