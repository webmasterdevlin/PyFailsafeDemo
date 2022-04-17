"""bffApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from shipping_api import views
from todo_api.views import (
    TodoApiView,
)

urlpatterns = [
    path('todos/<int:todo_id>', TodoApiView.as_view()),
    path('shipping/<int:shipping_id>', views.shipping),
]

urlpatterns = format_suffix_patterns(urlpatterns)
