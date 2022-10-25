from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from logistics import views

app_name = 'logistics'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('services/',views.Services.as_view(),name='services'),
    path('blog/',views.Blog.as_view(),name='blog'),
    path('industries/',views.Industries.as_view(),name='industries'),
    path('contact/',views.Contact.as_view(),name='contact'),
]
