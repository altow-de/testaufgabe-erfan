from django.db import models

class Company(models.Model):
    Name = models.CharField(max_length=40)

class JobPosting(models.Model):
    Title = models.CharField(max_length=40)
    Description = models.TextField(max_length=2000)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Applicant(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    JobPosting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)


