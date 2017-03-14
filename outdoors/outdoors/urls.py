from django.conf.urls import url
from django.contrib import admin

from events import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^trails/', views.trails, name='trails'),
    url(r'^traffic/', views.traffic, name='traffic'),
]
