from django.urls import path, include
from . import views

urlpatterns = [
	path('groups', views.Group.as_view())
]
