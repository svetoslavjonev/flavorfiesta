from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django_project.profiles.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
	form = UserEditForm
	add_form = UserCreateForm
	fieldsets = (
		("User info", {"fields": ("username", "password")}),
		("Personal info", {"fields": ("email", "first_name", "last_name",  "birth_date", "gender")}),
		("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",), },),
		("Important dates", {"fields": ("last_login", "date_joined")}),
	)
	list_display = ('username', 'email', 'is_staff', 'get_groups')

	def get_groups(self, obj):
		return ", ".join([group.name for group in obj.groups.all()])

	get_groups.short_description = 'Groups'