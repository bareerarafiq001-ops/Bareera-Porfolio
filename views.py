from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

from .forms import ContactForm, ServiceRequestForm, RegisterForm
from .models import (
    Home,
    About,
    Project,
    Service,
    Contact,
    ServiceRequest
)


# ================= HOME =================
def home(request):
    home = Home.objects.first()
    return render(request, 'portfolio/home.html', {
        'home': home
    })


# ================= ABOUT =================
def about(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {
        'about': about
    })


# ================= PROJECTS =================
def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {
        'projects': projects
    })


# ================= CONTACT =================
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {
        'form': form
    })


# ================= SERVICES =================
def services(request):
    services = Service.objects.all()

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request submitted successfully!')
            return redirect('services')
    else:
        form = ServiceRequestForm()

    return render(request, 'portfolio/services.html', {
        'form': form,
        'services': services
    })


# ================= REGISTER =================
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'portfolio/register.html', {
        'form': form
    })


# ================= LOGIN =================
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'portfolio/login.html')


# ================= LOGOUT =================
def user_logout(request):
    logout(request)
    return redirect('home')


# ================= DASHBOARD =================
@login_required(login_url='/login/')
def dashboard(request):
    contacts = Contact.objects.all().order_by('-created_at')
    service_requests = ServiceRequest.objects.all().order_by('-created_at')

    context = {
        'contacts': contacts,
        'service_requests': service_requests,
        'total_contacts': contacts.count(),
        'total_services': service_requests.count(),
    }

    return render(request, 'portfolio/dashboard.html', context)


# ================= SEARCH =================
def search(request):
    query = request.GET.get('q', '')

    project_results = Project.objects.filter(title__icontains=query)
    service_results = Service.objects.filter(title__icontains=query)

    return render(request, 'portfolio/search.html', {
        'query': query,
        'project_results': project_results,
        'service_results': service_results,
    })


# ================= API PROJECTS =================
def api_projects(request):
    projects = Project.objects.all()

    data = {
        "projects": [
            {
                "id": p.id,
                "title": p.title,
                "description": p.description,
                "github": p.github,
                "live_demo": p.live_demo,
            }
            for p in projects
        ]
    }

    return JsonResponse(data)


# ================= API CONTACT =================
@csrf_exempt
def api_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            Contact.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                message=data.get('message')
            )

            return JsonResponse({
                'status': 'success',
                'message': 'Message saved!'
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })

    return JsonResponse({
        'status': 'error',
        'message': 'POST request required'
    })