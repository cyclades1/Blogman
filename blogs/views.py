from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from .models import Blog
from django.contrib import messages
from .forms import SubmitForm

# Create your views here.

def index(request, *agrs, **kwargs):
	obj = Blog.objects.filter(private=False)
	context={
		"blogs":obj
	}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))
	# return HttpResponse("this is the home page")


def about(request, *agrs, **kwargs):
	form = SubmitForm()
	context={
		"form":form,
	}
	return render(request, 'about.html', context)

def logout_user(request):
	logout(request)
	messages.success(request, 'logged out successfully..')
	return redirect('/')

def login_view(request, *agrs, **kwargs):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user is not None :
			login(request, user)
			messages.success(request, 'Logged in successfully..')
			return redirect('/')
		else :
			messages.success(request, 'Username and Password did not match..')
			return render(request, 'login.html')
	elif(request.user.is_anonymous and request.method=="GET"):
		return render(request, 'login.html')
	return redirect('/profile')


def profile(request, *agrs, **kwargs):
	obj = Blog.objects.filter(author= request.user.username)
	context={
		"Public_blogs":obj.filter(private=False),
		"Private_blogs":obj.filter(private=True)
	}
	return render(request, 'profile.html', context)

def blog_page(request, *agrs, **kwargs):

	if request.method == "POST":
		author = request.user.username
		title = request.POST.get('title')
		content = request.POST.get('content')
		genre = request.POST.get('genre')
		private = bool(request.POST.get('private'))
		obj = Blog.objects.create(author=author, title=title,genre = genre, content=content, private=private)
		messages.success(request, 'Your blog posted..')
	elif request.user.is_anonymous:
		messages.success(request, 'You need too Login first..')
		return redirect('/login') 
	return render(request, 'blog.html')
