from django.conf.urls import url
from django.contrib import admin

from events import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^events_trails/', views.events_trails, name='events_trails'),
    url(r'^events_traffic/', views.events_traffic, name='events_traffic'),
    url(r'^venues/$', views.venues, name='venues'),
    url(r'^venues/(?P<pk>\d+)/$', views.venues_detail, name='venues_detail'),    
    url(r'^events/$', views.events, name='events'),
    url(r'^traffic/$', views.traffic, name='traffic'),
]
