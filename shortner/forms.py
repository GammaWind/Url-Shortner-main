from django import forms
from .validators import validate_url,validate_url_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url,validate_url_com])


    





    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        
        # url = cleaned_data['url']
        
        # url_validator = URLValidator()
        
        # try:
        #     url_validator(url)
        # except:
        #     raise forms.ValidationError('Invalid URL for this field')    

        # print(url)

    # def clean_url(self):
        
    #     url_validator = URLValidator()
    #     url = self.cleaned_data['url']
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL for this field')    

    #     print(url)
          