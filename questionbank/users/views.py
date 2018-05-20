# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.ListCreateAPIView):
	queryset = models.CustomUser.objects.all()
	serializer_class = serializers.UserSerializer