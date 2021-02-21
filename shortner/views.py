from django import shortcuts
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, redirect,resolve_url
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from shortner.models import Krikurl
from django.urls import reverse
from .forms import SubmitUrlForm
from analytics.models import ClickEvent
from emailnotifications.models import userEmails

from django.core.mail import send_mail


# Create your views here.

def url_redirect_viewFBV(request, shortcode=None ,*args, **kwargs):
    
    
    #obj = Krikurl.objects.get(shortcode = shortcode)
    kjd = get_object_or_404(Krikurl, shortcode=shortcode)
    print(ClickEvent.objects.get_or_create_count(kjd))
    return HttpResponseRedirect( kjd.url)


class HomeView(View):
    def get(self,request,*args, **kwargs):
        get_form = SubmitUrlForm()
        context = {
            'title' : 'Short It !',
            'form' : get_form,

        }
        return render(request,'shortner/home.html',context)

    def post(self,request,*args, **kwargs):
        my_dict = {}
        my_dict.get('url')
        
        form = SubmitUrlForm(request.POST)
        context = {
            'title' : 'Short It !',
            'form' : form,

        }
        tempelate = 'shortner/home.html'
        
        if form.is_valid():
            created_by_email = form.cleaned_data.get('email')
            emailobj,create = userEmails.objects.get_or_create(email_ID = created_by_email)
            created_by = emailobj
            


            new_url = form.cleaned_data.get('url')
            obj, created = Krikurl.objects.get_or_create(url=new_url,createdBy = created_by)
            context={

                'object' : obj,
                'created' : created

            }
            if created:
                tempelate = 'success.html'
                #send email notification
                shorturl = obj.get_short_url()
                
                
                sent = send_mail(subject='Shortend URL',message='Hi, your shortned URL for ' + obj.url + ' is ' + shorturl
                ,recipient_list=[created_by_email],from_email='urllshort5@gmail.com')
                print(sent)
                print('here')

            else:
                tempelate = 'already-exist.html'
    
        

        return render(request,tempelate, context)    




class url_redirect_viewCBV(View):
    def get(self,request, shortcode=None ,*args, **kwargs):
        print('hello')
        obj_url = None
        obj = get_object_or_404(Krikurl,shortcode=shortcode)
        obj_url = obj.url
        print(ClickEvent.objects.get_or_create_count(obj))
        return HttpResponse('Hello {sc}'.format(sc=obj_url))