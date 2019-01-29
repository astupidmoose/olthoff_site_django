from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),	
	path('projects/', views.projects, name='projects'),	
	path('contact/', views.contact, name='contact'),	
	path('code/git/', views.git, name='git'),	
	path('code/server_setup/', views.server_setup, name='server_setup'),	
	path('code/wordpress/', views.wordpress, name='wordpress'),	
]
