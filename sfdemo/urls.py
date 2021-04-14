from django.contrib import admin
from django.urls import path,include
from app import views
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserRegisterView,name='index'),
    path('detail/',views.allusers,name='alluser'),
    #inbuilt_email_url
    path('email/', include(email_urls)),
    path('api/', include('app.api.urls')),
]
