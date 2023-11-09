"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),  # path('경로', 뷰 함수): If the user access 경로, Django executes 뷰 함수
    path("api/v1/rooms/", include("rooms.urls")), # path('경로', include("애플리케이션명.urls")): If the user access 경로, Django enters the 애플리케이션`s urls.py file
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls"))
]
