from django.urls import path
from .views import JobDescriptionView

urlpatterns = [
    path('generate-job-description/', JobDescriptionView.as_view(), name='generate-job-description'),
]
