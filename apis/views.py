from django.shortcuts import render
from rest_framework import viewsets

from .models import Course, Candidate, Competencies, Education
from .models import Certification, Award, Skill, Experience
from .models import JobDescription, Industry

from .serializers import CourseSerializer, CandidateSerializer, CompetenciesSerializer, EducationSerializer
from .serializers import CertificationSerializer, AwardSerializer, SkillSerializer, ExperienceSerializer
from .serializers import JobDescriptionSerializer, IndustrySerializer, CommonSerializer

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CandidateViewset(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(id_email=candidateId)
        
        return queryset


class CompetenciesViewset(viewsets.ModelViewSet):
    queryset = Competencies.objects.all()
    serializer_class = CompetenciesSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)
        
        return queryset


class EducationViewset(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)
        
        return queryset


class CertificationViewset(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)
        
        return queryset

class AwardViewset(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)
        
        return queryset


class SkillViewset(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)

        return queryset


class ExperienceViewset(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)

        return queryset

class JobDescriptionViewset(viewsets.ModelViewSet):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer


class IndustryViewset(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        candidateId = self.request.query_params.get('candidateId')

        if candidateId:
            queryset = queryset.filter(candidate__id=candidateId)

        return queryset


class CommonViewset(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CommonSerializer