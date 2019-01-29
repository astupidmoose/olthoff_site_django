from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def git(request):
	return render(request, "git.html", {})

def server_setup(request):
	return render(request, "server_setup.html", {})

def wordpress(request):
	return render(request, "wordpress.html", {})

def projects(request):
	return render(request, "projects.html", {})

def contact(request):
	return render(request, "contact.html", {})