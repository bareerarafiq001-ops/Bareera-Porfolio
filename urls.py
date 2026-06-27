from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/contact/', views.api_contact, name='api_contact'),
]
