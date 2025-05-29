# ApiDjango/tasks/urls.py

from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls')),
]


