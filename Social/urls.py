"""Social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

admin.site.site_header = "Social Admin"
admin.site.site_title = "Social Admin Portal"
admin.site.index_title = "Welcome to Social Portal"

# serializer for API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']


# Viewset to define the behavior of view
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer;


# Router for autometic URL config
router = routers.DefaultRouter()
router.register(r'users',UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
    path('api/', include(router.urls)),
    path('user-info/', include('rest_framework.urls', namespace='rest_framework'))
]
