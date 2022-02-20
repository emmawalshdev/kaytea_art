from django.urls import path
from .views import privacy_view, terms_view

urlpatterns = [
    path('privacy/', privacy_view, name="privacy"),
    path('terms/', terms_view, name="terms"),
]
