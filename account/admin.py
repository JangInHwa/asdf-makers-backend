from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('email', 'username', 'is_active', 'is_superuser', 'date_joined', 'id')
	list_display_links = ('email',)
	list_filter = ('is_superuser', 'is_active',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('username',)}),
		('Permissions', {'fields': ('is_active', 'is_superuser',)}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	search_fields = ('email','username')
	ordering = ('-date_joined',)
	filter_horizontal = ()

admin.site.register(User, UserAdmin)
