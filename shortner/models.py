from UrlShort.settings import SHORTCODE_MAX
from django.db import models
from  django.conf import settings
from .validators import validate_url,validate_url_com
from django_hosts.resolvers import reverse

from .utils import create_shortcode,code_generater
SHORTCODE_MAX = getattr(settings,'SHORTCODE_MAX',15)



# Create your models here.
class KrikurlManager(models.Manager):
    def all(self, *args, **kwargs):
        
        qs_orignal = super(KrikurlManager, self).all( *args, **kwargs)
        qs = qs_orignal.filter()
        return qs

    def refresh_shortcodes(self):
        qs = Krikurl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        






class Krikurl(models.Model):
    url = models.CharField(max_length = 220, validators=[validate_url,validate_url_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = KrikurlManager()


    def save(self,*args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(Krikurl, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)

    def __unicoed__(self):
        return str(self.url)   

    def get_short_url(self):
        short_url = reverse('scode',kwargs={'shortcode' : self.shortcode}, host='urllshort',scheme='http')
        return short_url

