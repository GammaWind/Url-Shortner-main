from django.db import models

from shortner.models import Krikurl

# Create your models here.
class ClickEventManager(models.Manager):
    def get_or_create_count(self, instance):
        if isinstance(instance , Krikurl):
            obj ,created = self.get_or_create(krik_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None    


class ClickEvent(models.Model):
    krik_url = models.OneToOneField(Krikurl,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = ClickEventManager()

    def __str__(self):
        return '{c}'.format(c=self.count)
