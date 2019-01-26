from django.conf.urls import url

from . import views

app_name = 'trading'

urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
]
