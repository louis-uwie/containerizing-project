"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin stuff
    path('admin/', admin.site.urls),
    path('', include('user_management.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path("hobbysite", include("homepage.urls")),

    # apps
    path('merchstore/', include('merchstore.urls')), 
    path('wiki/', include('wiki.urls')), 
    path('blog/', include('blog.urls', namespace="blog")), 
    path('commissions/', include("commissions.urls", namespace="commissions"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# user uploaded stuff / basically what we use Pillow for
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
