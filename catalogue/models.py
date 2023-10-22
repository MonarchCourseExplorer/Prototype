from django.db import models
from users.models import Student, Professor

class Course(models.Model):
    name = models.CharField('Course Name', max_length= 120)
    department = models.CharField(max_length=120)
    description = models.TextField(blank= True)

    def __str__(self):
        return self.name
    


class Section(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    courseID = models.IntegerField()
    semester = models.CharField('Semester', max_length=50)
    session = models.CharField('Session', max_length=25)
    offeringTime = models.TimeField(auto_now=False, auto_now_add=False)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)
    deliveryType = models.CharField(max_length=25)
    meetingType = models.CharField(max_length=25)

    def __str__(self):
        return self.course + " " + self.professor.first_name + " " + self.professor.last_name


class Syllabus(models.Model):
    SectionID = models.ForeignKey(Section,on_delete= models.CASCADE)
    OrginalLocation = models.CharField('Orginal Location', max_length = 120)
    NormalizedLocation = models.CharField('Normalized Location', max_length=120)

    def __str__(self):
        return  "Syllabus for " + self.SectionID



class Feedback(models.Model):
    SectionID = models.ForeignKey(Section,on_delete= models.CASCADE)
    #StudentID = models.IntegerField('StudentID')
    StudentID = models.ForeignKey(Student, on_delete= models.CASCADE)
    ProfessorID = models.ForeignKey(Professor, on_delete= models.CASCADE)
    Review =  models.TextField(blank= True)
    Rating = models.IntegerField(blank=True)

    def __str__(self):
        return "Feedback for " + self.SectionID