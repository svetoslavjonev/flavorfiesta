from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('django_project.common.urls')),
	path('profiles/', include ('django_project.profiles.urls')),
	path('events/', include ('django_project.events.urls')),
	path('chefs/', include ('django_project.chefs.urls')),
	path('venues/', include ('django_project.venues.urls')),
	path('occasions/', include ('django_project.occasions.urls')),
	path('bookings/', include ('django_project.bookings.urls')),
	path('tickets/', include ('django_project.tickets.urls')),
	path('api/', include ('django_project.api.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
	urlpatterns += [
		re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
	]