from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def git(request):
	return render(request, "code/git.html", {})

def server_setup(request):
	return render(request, "code/server_setup.html", {})

def wordpress(request):
	return render(request, "code/wordpress.html", {})

def django(request):
	return render(request, "code/django.html", {})

def python(request):
	return render(request, "code/python.html", {})

def contact(request):
	return render(request, "contact.html", {})