from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    re_path(r'^$', RedirectView.as_view(url='/login/', permanent=False)),
]
