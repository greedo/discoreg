from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("callback", views.callback, name="callback"),
    path("link", views.link, name="link"),
    path("webhook", views.webhook_handler, name="webhook"),
]
