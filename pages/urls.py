from django.urls import path
from .views import privacy_view

urlpatterns = [
    path('privacy/', privacy_view, name="privacy"),
]
