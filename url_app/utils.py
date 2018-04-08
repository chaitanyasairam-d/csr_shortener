import random,string
from django.conf import settings
# from shortener.models import UrlShortener doesnt work as this file is a importing file to the models.py file
SHORTCODE_MIN = settings.SHORTCODE_MIN

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.ascii_uppercase +string.digits):
    #new_code=''
    #for _ in range(size):
    #    new_code = random.choice(chars)
    #return new_code
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    from url_app.models import UrlShortener
    sc_exists = UrlShortener.objects.filter(shortcode=new_code).exists()

    if sc_exists:
        return create_shortcode(size=size)
    return new_code
