"""disseminate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from app.views import DisplayListView, DisplayCreateView, DisplayUpdateView, DisplayDeleteView, FileCreateView, assign_file_to_display, FileListView, manage_file_assignments, FileDeleteView

urlpatterns = [
    path('', lambda request: redirect('file-list', permanent=False)),  # Redirect root URL to /files/
    path('admin/', admin.site.urls),
    path('displays/', DisplayListView.as_view(), name='display-list'),
    path('displays/add/', DisplayCreateView.as_view(), name='display-add'),
    path('displays/<int:pk>/edit/', DisplayUpdateView.as_view(), name='display-edit'),
    path('displays/<int:pk>/delete/', DisplayDeleteView.as_view(), name='display-delete'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/upload/', FileCreateView.as_view(), name='file-upload'),
    path('files/<int:file_id>/assign/', manage_file_assignments, name='manage-file-assignments'),
    path('files/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    quit()
