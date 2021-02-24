from django.core import validators
from django.db import models
from .validators import validate_Email





# Create your models here.
class ClickEventManager(models.Manager):
    def get_or_saveEmail(self, emailaddress):
        
        obj ,created = self.get_or_create(email_ID = emailaddress)

        return obj.email_ID
           


class userEmails(models.Model):
    
    email_ID = models.EmailField(max_length=254,validators=[validate_Email],null=False,unique=True)
    id = models.AutoField(primary_key=True)
    
    objects = ClickEventManager()

    def __str__(self):
        return '{c}'.format(c=self.email_ID)

