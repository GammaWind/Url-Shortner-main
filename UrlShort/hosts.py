from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'urllshort', settings.ROOT_URLCONF, name='urllshort'),  # <-- The `name` we used to in the `DEFAULT_HOST` setting
    host(r'(?!urllshort).*', 'UrlShort.hostsconf.urls', name='wildcard'),
)