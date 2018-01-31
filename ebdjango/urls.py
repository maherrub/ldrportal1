"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from api.resources import *

ticket_resource = TicketResource()
project_resource = LdrprojectResource()

#Admin Configuration
admin.site.site_header = settings.ADMIN_SITE_HEADER

#original pattern
#urlpatterns = [
#   url(r'^admin/', admin.site.urls),
#   url(r'^', include('helloworld.urls')), 
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('portal.urls')),
    url(r'^up/', include('userapp.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^helpdesk/', include('helpdesk.urls', namespace='helpdesk')),
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^api/', include(ticket_resource.urls)),
    url(r'^api/', include(project_resource.urls)),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)