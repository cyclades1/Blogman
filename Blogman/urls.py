"""Blogman URL Configuration

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
from django.contrib.auth.models import User
from blogs.models import Blog

#DRF imports
from rest_framework import routers, serializers, viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

admin.site.site_header = "Blogman Admin"
admin.site.site_title = "Blogman Admin Portal"
admin.site.index_title = "Welcome to Blogman Portal"

# serializer for API representation
class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model     = User
		fields    = ['username', 'email']


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Blog
        fields = ['title','author', 'content', 'date', 'genre']

    

# Viewset to define the behavior of view

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    http_method_names = ['get',]
    def list(self, request):

        queryset    = User.objects.filter(is_staff=False)
        serializer  = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        data ={}
        data['Failure']="This method is not allowed"
        return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class BlogViewSet(viewsets.ModelViewSet):

    queryset            = Blog.objects.filter(private=False)
    serializer_class    = BlogSerializer
    http_method_names   = ['get',]


# connecting the ViewSets

user_list = UserViewSet.as_view({'get': 'list'})



# Router for autometic URL config
router    = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'blogs',BlogViewSet, basename='blogs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
    path('api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
