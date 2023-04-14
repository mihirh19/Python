
from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Mihir Admin"
admin.site.site_title = "Mihir Admin Portal"
admin.site.index_title = "Welcome to iceream admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/',views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
