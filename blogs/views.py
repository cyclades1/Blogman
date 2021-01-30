from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from .models import Blog
from django.contrib import messages
from .forms import SubmitForm
from django.contrib.auth.decorators import login_required



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
	return redirect('/')


def signup(request, *args, **kwargs):

	if(request.user.is_anonymous and request.method=="GET"):
		return render(request, 'login.html')

	elif request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(first_name, last_name, username, email, password)
		if bool(User.objects.filter(email=email)):
			messages.success(request, "User already exist..")
			return redirect('/login')
		user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
		login(request, user)
		messages.success(request, "Your account is active now..")
		return redirect('/')
	
@login_required
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
		messages.success(request, 'You need to Login first..')
		return redirect('/login') 
	return render(request, 'blog.html')


def desc(request, id, *args, **kwargs):
	try:
		blog = Blog.objects.get(id = id)
		context={
			'blog':blog
		}
	except Exception as e:
		messages.success(request, "Not a valid blog..")
		return redirect('/')
		
	return render(request,'desc.html', context)
	# return HttpResponse(id)