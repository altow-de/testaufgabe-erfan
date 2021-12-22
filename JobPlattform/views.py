from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company, JobPosting, Applicant
from .serializer import CompanySerializer, JobPostingSerializer, ApplicantSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print('---Create---')
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = super().destroy(request, *args, **kwargs)
        print('---Destroy : {}'.format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = super().retrieve(request, *args, **kwargs)
        print('---Retrieve : {}'.format(instance.name))
        return obj


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print('---Create---')
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = super().destroy(request, *args, **kwargs)
        print('---Destroy : {}'.format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = super().retrieve(request, *args, **kwargs)
        print('---Retrieve : {}'.format(instance.name))
        return obj


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print('---Create---')
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = super().destroy(request, *args, **kwargs)
        print('---Destroy : {}'.format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        obj = super().retrieve(request, *args, **kwargs)
        print('---Retrieve : {}'.format(instance.name))
        return obj


