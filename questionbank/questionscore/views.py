# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from users.serializers import UserSerializer

from rest_framework.decorators import api_view

from django.contrib.auth import authenticate, login, logout


def createuser(request):
	print 'entrouuu'
	return render(request, 'questionscore/createuser.html')

@api_view(["POST"])
def saveuser(request):
	serialized = UserSerializer(data=request.data)
	if serialized.is_valid():
		serialized.save()
		return render(request, 'questionscore/login.html')
	else:
		return render(request, 'questionscore/createuser.html')

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'questionscore/land_page.html')
			else:
				return render(request, 'questionscore/login.html')
		else:
			return render(request, 'questionscore/login.html')
	else:
		return render(request, 'questionscore/login.html')

def logout_user(request):
	logout(request)
	return redirect('/questionscore/login/')