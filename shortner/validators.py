from django.core.validators import URLValidator, validate_email
from django.core.exceptions import ValidationError


def validate_url(value):
        url_validater = URLValidator()
        val1_invalid = False
        val2_invalid = False
        try:
            url_validater(value)
        except:
            val1_invalid = True
        val2 = 'http://' + value

        try:
            url_validater(val2)
        except:
            val2_invalid= True
        if val1_invalid == False and val2_invalid == False:
               
            raise ValidationError('Invalid Url for this filed')
        return value

def validate_url_com(value):
        if not 'com' in value:
            raise ValidationError('Invalid Url for this filed beacuse of no com')
        return value