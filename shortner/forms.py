from django import forms
from .validators import validate_url,validate_url_com
from emailnotifications.validators import validate_Email

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url])
    email = forms.EmailField(label='Enter your Email', validators=[validate_Email])


    





    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        cleaned_data = super(SubmitUrlForm, self).clean()
        
        if self.is_valid():
            url = self.cleaned_data['url']
            newurl = validate_url(url)
            self.cleaned_data['url'] = newurl
        
       

    # def clean_url(self):
        
    #     url_validator = URLValidator()
    #     url = self.cleaned_data['url']
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL for this field')    

    #     print(url)
          