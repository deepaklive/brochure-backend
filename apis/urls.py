from django.urls import include, path
from rest_framework import routers

from .views import CourseViewSet, CandidateViewset, CompetenciesViewset, EducationViewset
from .views import CertificationViewset, AwardViewset, SkillViewset, ExperienceViewset
from .views import JobDescriptionViewset, CommonViewset

router = routers.DefaultRouter()

router.register(r'course', CourseViewSet)
router.register(r'candidate', CandidateViewset, basename='candidateview')
router.register(r'competencies', CompetenciesViewset)
router.register(r'education', EducationViewset)
router.register(r'certification', CertificationViewset)
router.register(r'award', AwardViewset)
router.register(r'skill', SkillViewset)
router.register(r'experience', ExperienceViewset)
router.register(r'jd', JobDescriptionViewset)
router.register(r'commonview', CommonViewset, basename='commonview')


urlpatterns = [
    path('', include(router.urls)),
]