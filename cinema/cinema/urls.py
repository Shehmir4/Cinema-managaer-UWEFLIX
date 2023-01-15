"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from cinema import views

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),

    # Home page
    path("", views.home, name="home"),
    path("home/", views.home),
    #path("cinema/home/", views.home),

    # Add club page
    path("addclub/", views.addclub, name="addclub"),

    # Delete club page
    path("delete-std/<int:id>/", views.delete_data, name="deletedata"),

    # Update club page
    path("update-std/<int:id>/", views.update_data),
    path("do_update_std/<int:id>/", views.do_update_std,name="do_update_std"),
    path("home/update-std/<int:id>/", views.update_data),
    path("home/do_update_std/<int:id>/", views.do_update_std,name="do_update_std"),
]

