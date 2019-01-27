from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'trading'

urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url('^portfolio$', login_required(views.PortfolioView.as_view()), name='portfolio'),
]
