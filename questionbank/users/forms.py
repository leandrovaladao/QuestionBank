# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

	class meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields