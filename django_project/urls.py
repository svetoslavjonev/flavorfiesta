from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('django_project.common.urls')),
	path('profiles/', include ('django_project.profiles.urls')),
	path('events/', include ('django_project.events.urls')),
	path('chefs/', include ('django_project.chefs.urls')),
	path('venues/', include ('django_project.venues.urls')),
	path('occasions/', include ('django_project.occasions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
