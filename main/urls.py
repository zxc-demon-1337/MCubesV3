from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    # path('test', views.test, name='test'),
    # path('account', views.account, name='account')
]