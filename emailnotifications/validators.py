from django.core.validators import URLValidator,EmailValidator

from django.core.exceptions import ValidationError 



def validate_Email(value):
        email_validater = EmailValidator()
        
        try:
            email_validater(value)
        except:
            
            raise ValidationError('Invalid Email')
               

        
           
        return value