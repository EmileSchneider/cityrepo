from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response  import Response
from .models import LandingPage, LandingPageSerializer, Education, EducationSerializer, WorkExperience, WorkExperienceSerializer 


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class CVView(APIView):
    def get(self, request, format=None):
        e = WorkExperience.objects.all()
        s = WorkExperienceSerializer(e, many=True)
        ed = Education.objects.all()
        eds = EducationSerializer(ed, many=True)
        data = [s.data, eds.data]
        return Response(data)  

class LandingPageView(APIView):
    def get(self, request, format=None):
        p = LandingPage.objects.get()
        s  = LandingPageSerializer(p)
        return Response(s.data)
