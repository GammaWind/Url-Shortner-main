from django.conf.urls import url
from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),
    # re_path(r'^a/(?P<shortcode>[\w-]+)/$',url_redirect_viewCBV,name=url_redirect_viewCBV),
    # re_path(r'^b/(?P<shortcode>[\w-]+)/$',url_redirect_viewFBV,name='url_redirect_viewFBV'),
    
     
]