from django.urls import path
from rest_framework.routers import DefaultRouter
from JobPlattform import views

router = DefaultRouter()
router.register('company/', views.CompanyViewSet, basename='Company')
router.register('jobposting/', views.JobPostingViewSet, basename='JobPosting')
router.register('applicant/', views.ApplicantViewSet, basename='Applicant')

urlpatterns = []

urlpatterns += router.urls









