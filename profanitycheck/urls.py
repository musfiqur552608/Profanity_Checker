from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('check.urls')),
    path('profanityapi/', views.ProfanityApi.as_view())
]
