from django.urls import path, include
from . import views

urlpatterns = [
	path('groups', views.GroupView.as_view()),
	path('groups/<int:pk>', views.GroupDetailView.as_view())
]
