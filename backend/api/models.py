from django.db import models
from rest_framework import serializers

class LandingPage(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    topAccomplishments = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    github = models.CharField(max_length=200)

class WorkExperience(models.Model):
    employer = models.CharField(max_length=200)
    work = models.CharField(max_length=2000)


class WorkExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ('employer', 'work')

class Education(models.Model):
    institution = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('institution', 'description')

class LandingPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LandingPage
        fields = ('firstName', 'lastName', 'description', 'github', 'topAccomplishments')
    
