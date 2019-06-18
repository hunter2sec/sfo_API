"""jwt_secrets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from django.urls import include, path
from accounts import views as auth_views

from django.contrib import admin
from rest_framework_jwt import views as jwt_views
from core import views

from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', auth_views.signup, name='signup'),
    url(r'^api/', include(router.urls)),
    url(r'^api/token/get/$', jwt_views.obtain_jwt_token, 
    name='get_token'),
    url(r'^api/token/refresh/$', jwt_views.refresh_jwt_token, 
    name='refresh_token'),
    url(r'^api/token/verify/$', jwt_views.verify_jwt_token, 
    name='verify_token'),
    path('', auth_views.home, name='home')
] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
