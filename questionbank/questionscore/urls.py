# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'/createuser/', views.createuser, name='teste'),
	url(r'/saveuser/', views.saveuser, name='createuser'),
	url(r'/login/', views.login_user, name='login'),
	url(r'/logout/', views.logout_user, name='logout'),
]