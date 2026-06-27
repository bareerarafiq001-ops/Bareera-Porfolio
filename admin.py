from django.contrib import admin
from .models import (
    Home,
    About,
    Project,
    Service,
    Contact,
    ServiceRequest
)

# ---------------- Home ----------------
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading')


# ---------------- About ----------------
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)


# ---------------- Projects ----------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


# ---------------- Services ----------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


# ---------------- Contact ----------------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email'
    '')
    list_filter = ('created_at',)


# ---------------- Service Requests ----------------
@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'service',
        'budget',
        'created_at'
    )
    search_fields = ('name', 'email')
    list_filter = ('service', 'created_at')