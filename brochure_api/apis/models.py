from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=25, null=False)
    course_name = models.CharField(max_length=100, null=False)
    institute_name = models.CharField(max_length=100, null=False)
    institute_location = models.CharField(max_length=50, null=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
          return self.course_name



class Candidate(models.Model):
    course = models.PositiveIntegerField(null=False, default=0)
    name = models.CharField(max_length=50, null=False)
    rank = models.CharField(max_length=25, null=True, blank=True)
    service = models.CharField(max_length=20, null=True, blank=True)
    experience = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=10, null=False)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    linkedIn = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)

    # ROLE 
    hrm_role = models.BooleanField(default=False)
    scm_role = models.BooleanField(default=False)
    operation_role = models.BooleanField(default=False)
    project_role = models.BooleanField(default=False)
    security_role = models.BooleanField(default=False)
    admin_role = models.BooleanField(default=False)
    it_role = models.BooleanField(default=False)
    aviation_role = models.BooleanField(default=False)

    #INDUSTRY

    def __str__(self):
          return self.name


class Competencies(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="competencies", on_delete=models.CASCADE)
    core_competencies = models.CharField(max_length=50, null=False)
    percentage = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.core_competencies


class Education(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="education", on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100, null=False)
    institute = models.CharField(max_length=100, null=False)
    year = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.qualification


class Certification(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="certification", on_delete=models.CASCADE)
    certificate = models.CharField(max_length=100, null=False)
    institute = models.CharField(max_length=100, null=False)
    valid_upto = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.certificate


class Award(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="awards", on_delete=models.CASCADE)
    award = models.TextField(null=False)
    
    def __str__(self):
          return self.award

class Skill(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="skills", on_delete=models.CASCADE)
    skill = models.CharField(max_length=50, null=False)
    percentage = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
          return self.skill



class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="experiences", on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=False)
    org_name = models.CharField(max_length=100, null=True, blank=True)
    org_location = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True)

    

    def __str__(self):
          return self.role


class JobDescription(models.Model):
    role = models.ForeignKey(Experience, related_name="jobdescription", on_delete=models.CASCADE)
    jd = models.TextField(null=False)

    def __str__(self):
          return self.jd

