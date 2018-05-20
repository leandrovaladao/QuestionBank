# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
	url('users/', include('users.urls')),
	url('rest-auth/', include('rest_auth.urls')),
	url('rest-auth/registration/', include('rest_auth.registration.urls'))
]