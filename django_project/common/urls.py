from django.urls import path
from django_project.common.views import IndexView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
]
