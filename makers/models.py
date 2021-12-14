from django.db import models
from django.db.models.deletion import SET_NULL
from config.settings import base as settings
from account.models import User

# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	expected_period_start = models.DateField(null=True)
	expected_period_end = models.DateField(null=True)
	created = models.DateTimeField(editable=False, auto_now_add=True)


#분야를 나타냄 Flutter, Django 등등..
class Field(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self) -> str:
		return self.title
		
#프로젝트 지원 상태를 나타냄
class Application(models.Model):
	REQUESTED = 'REQUESTED'
	MEMBER = 'MEMBER'
	ADMIN = 'ADMIN'
	POSITION_CHOICES = (
		(REQUESTED, 'requested for participation'),
		(MEMBER, 'member'),
		(ADMIN, 'admin who has permissions')
	)
	WAITING = 'WAITING'
	IN_PROGRESS = 'IN_PROGRESS'
	DONE = 'DONE'
	PROGRESS_STATUS_CHOICES = (
		('WAITING', 'wating for open'),
		('IN_PROGRESS', 'project is working on it'),
		('DONE', 'project is done')
	)

	applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
	field = models.ForeignKey(Field, null=True, on_delete=models.SET_NULL)
	group = models.ForeignKey(Group, related_name='applications', on_delete=models.CASCADE)
	postion = models.CharField(max_length=10, choices=POSITION_CHOICES, default=REQUESTED)
	progress_status = models.CharField(max_length=20, choices=PROGRESS_STATUS_CHOICES, default=WAITING)
