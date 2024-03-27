from django import forms
from django.conf import settings
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
	class Meta:
		model = UserModel
		fields = ('username', 'email', 'password1', 'password2')
		field_classes = {'username': auth_forms.UsernameField}


class UserEditForm(auth_forms.UserChangeForm):
	class Meta:
		model = UserModel
		fields = '__all__'
		field_classes = {"username": auth_forms.UsernameField}

		widgets = {
			'birth_date': forms.widgets.DateInput(attrs={'type': 'date'})
		}

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = ('email', 'first_name', 'last_name', 'birth_date', 'gender')

		widgets = {
			'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
		}

		labels = {
			'birth_date': "Birthday",
		}
