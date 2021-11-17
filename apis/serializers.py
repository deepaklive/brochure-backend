from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.relations import ManyRelatedField

from .models import Course, Candidate, Competencies, Education, Role
from .models import Certification, Award, Skill, Experience
from .models import JobDescription, Industry


# User
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = fields = '__all__'


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencies
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = fields = '__all__'


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = fields = '__all__'


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = fields = '__all__'


class CommonSerializer(serializers.ModelSerializer):

    competency = CompetenciesSerializer(source='competencies', many=True, read_only=True)
    edn = EducationSerializer(source='education', many=True, read_only=True)
    certificate = CompetenciesSerializer(source='certification', many=True, read_only=True)
    awrd = AwardSerializer(source='awards', many=True, read_only=True)
    skl = SkillSerializer(source='skills', many=True, read_only=True)
    expernc = ExperienceSerializer(source='experiences', many=True, read_only=True)
    # rl = RoleSerializer(source='roles', many=True)
    # indst = IndustrySerializer(source='industries', many=True)

    class Meta:
        model = Candidate
        fields = [
    'id_email', 
    'course',
    'name',
    'rank',
    'service',
    'experience',
    'qualification',
    'gender',
    'phone_no',
    'email',
    'linkedIn',
    'image_url',
    'introduction',
    'hrm_role',
    'scm_role',
    'operation_role',
    'project_role',
    'security_role',
    'admin_role',
    'it_role',
    'aviation_role',
    'competency',
    'edn',
    'certificate',
    'awrd',
    'skl',
    'expernc',
    # 'rl',
    # 'indst'
    ]
