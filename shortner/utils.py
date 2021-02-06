from UrlShort.settings import SHORTCODE_MIN
import random
import string
from  django.conf import settings


SHORTCODE_MIN = getattr(settings,'SHORTCODE_MIN',6)
SHORTCODE_MAX = getattr(settings,'SHORTCODE_MAX',15)
def code_generater(size = SHORTCODE_MIN , chars = string.ascii_lowercase + string.digits ):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code = code_generater(size=SHORTCODE_MIN)
    Modelinstance = instance.__class__
    qs_ifexists = Modelinstance.objects.filter(shortcode=new_code).exists()
    if qs_ifexists:
        return create_shortcode(size=SHORTCODE_MIN)
    return new_code    