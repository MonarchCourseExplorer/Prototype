from django.db import models

class Course(models.Model):
    name = models.CharField('Course Name', max_length= 120)
    department = models.CharField(max_length=120)
    description = models.TextField(blank= True)

    def __str__(self):
        return self.name
    

class Syllabus(models.Model):
    SectionID = models.IntegerField('SectionID')
    OrginalLocation = models.CharField('Orginal Location', max_length = 120)
    NormalizedLocation = models.CharField('Normalized Location', max_length=120)

    def __str__(self):
        return self.SectionID
    
    

class Feeback(models.Model):
    SectionID = models.IntegerField('SectionID')
    StudentID = models.IntegerField('StudentID')
    Review =  models.TextField(blank= True)
    Rating = models.IntegerField(blank=True)

    def __str__(self):
        return self.SectionID
    

class Section(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    courseID = models.IntegerField()
    semester = models.CharField('Semester', max_length=50)
    session = models.CharField('Session', max_length=25)
    offeringTime = models.TimeField(auto_now=False, auto_now_add=False)
    professor = models.CharField('Professor Name', max_length=120)
    deliveryType = models.CharField(max_length=25)
    meetingType = models.CharField(max_length=25)

    def __str__(self):
        return self.name