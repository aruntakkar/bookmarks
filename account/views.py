from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username = cd['username'], password = cd['password'])
			if user is not None:
				if user.is_active:
					# if user is active, we log the user into website.
					# we set the user in the session by calling the login() method.
					login(request, user)
					return HttpResponse('Authenticated ' 'successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})

"""
	if the user is not authenticated, it redirects him to the login URL with
	the URL he was trying to access as a GET parameter named next.

	By doing so, the log in view redirects the user back to the URL he was trying
	to access after he is successfully logged in.
"""

"""
	We also define a section variable , We are going to use this variable to track
	which section of the site the user is watching, Multiple views may correspond
	to the same section,

	This is simple way to define which section each view corresponds to.
"""
