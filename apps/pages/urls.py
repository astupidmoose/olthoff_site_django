from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),	
	path('contact/', views.contact, name='contact'),	
	path('code/git/', views.git, name='git'),	
	path('code/server_setup/', views.server_setup, name='server_setup'),	
	path('code/wordpress/', views.wordpress, name='wordpress'),	
	path('code/python/', views.python, name='python'),	
	path('code/django/', views.django, name='django'),	
]
