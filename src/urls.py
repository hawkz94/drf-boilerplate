from django.conf.urls import include, url
from rest_framework.authtoken import views
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from profile.views import ProfileViewSet, CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, base_name="ProfileView")

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', CustomObtainAuthToken.as_view()),
    path('admin/', admin.site.urls),
]
