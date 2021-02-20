from django.core.validators import URLValidator,EmailValidator

from django.core.exceptions import ValidationError 


def validate_url(value):
        url_validater = URLValidator()
        
        try:
            url_validater(value)
        except:
            if not 'http://' in value:
                print(value)
                value = 'http://' + value
                print(value)
        try:
            url_validater(value)
                    
        except:
            
            raise ValidationError('Invalid Url')
               

        
        print(value)    
        return value

def validate_url_com(value):
        if not 'com' in value:
            raise ValidationError('Invalid Url for this filed beacuse of no com')
        return value