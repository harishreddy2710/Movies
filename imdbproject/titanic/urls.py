from django.urls import path
from rest_framework import routers

from .views import getById

router = routers.DefaultRouter()
urlpatterns = [
    path('<slug:slug>/', getById)

]