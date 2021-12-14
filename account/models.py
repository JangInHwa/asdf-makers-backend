from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, username, email, password, **extra_fields):
		if not email:
			raise ValueError('The given email must be set')
		if not username:
			raise ValueError('The given username must be set')
		user: User = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create(self, username, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	id = models.AutoField(primary_key=True)
	email = models.EmailField(verbose_name='email',
							  max_length=255,
							  unique=True)
	username = models.CharField(max_length=20)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(auto_now_add=True, blank=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'
		ordering = ['email']

	def __str__(self) -> str:
		return f'{self.username} : {self.email}'

	@property
	def is_staff(self):
		return self.is_superuser
