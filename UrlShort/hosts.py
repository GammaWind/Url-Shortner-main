from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    #prod
    
    # host(r'urllshort', settings.ROOT_URLCONF, name='urllshort'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
    # host(r'(?!urllshort).*', 'UrlShort.hostsconf.urls', name='wildcard'),
    
    #test
    host(r'www', settings.ROOT_URLCONF, name='www'), 
    host(r'(?!www).*', 'UrlShort.hostsconf.urls', name='wildcard'),



)