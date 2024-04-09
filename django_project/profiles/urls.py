from django.urls import path

from django_project.profiles.views import SignInUserView, SignUpUserView, signout_user, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('signin-user/', SignInUserView.as_view(), name='signin-user'),
	path('signout-user/', signout_user, name='signout-user'),
	path('signup-user/' , SignUpUserView.as_view(), name='signup-user'),
	path('details/<int:pk>', ProfileDetailsView.as_view(), name='profile-details'),
	path('edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
	path('delete/<int:pk>' , ProfileDeleteView.as_view(), name='profile-delete'),
]