from django.db import models

# Home Page
class Home(models.Model):
    heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=300)
    profile_image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.heading


# About Page
class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title


# Projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)

    def __str__(self):
        return self.title


# Services
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Contact Messages
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Service Requests
class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('web', 'Web Development'),
        ('design', 'Designing & Canva'),
        ('ai', 'AI & Computer Vision'),
        ('marketing', 'Digital Marketing'),
        ('ebook', 'eBook Writing'),
        ('dispatch', 'Truck Dispatch Training'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    budget = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name