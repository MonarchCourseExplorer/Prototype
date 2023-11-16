from django.db import models
from users.models import Student, Professor

#MCE Standard Databases
class Department(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField('Course Name', max_length= 120)
    department = models.CharField(max_length=120)
    description = models.TextField(blank= True)
    number = models.CharField('Course Number', max_length=10) #probably excessive, but it doesn't hurt
    credits = models.CharField(max_length=10) #We aren't doing anything with this, so leave it as char so 1-3 works

    def __str__(self):
        return self.name
    
class Section(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    #courseID = models.IntegerField() #is this the CRN?
    semester = models.CharField('Semester', max_length=50)
    session = models.CharField('Session', max_length=25)
    offering_time = models.CharField(255) # models.TimeField(auto_now=False, auto_now_add=False)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)
    delivery_type = models.CharField(max_length=25)
    meeting_type = models.CharField(max_length=25)
    crn = models.IntegerField()

    def __str__(self):
        return self.course + " " + self.professor.first_name + " " + self.professor.last_name

class Syllabus(models.Model):
    SectionID = models.ForeignKey(Section,on_delete= models.CASCADE)
    OrginalLocation = models.CharField('Orginal Location', max_length = 120)
    NormalizedLocation = models.CharField('Normalized Location', max_length=120)

    def __str__(self):
        return  "Syllabus for " + self.SectionID

#MCE Feedback
class Feedback(models.Model):
    SectionID = models.ForeignKey(Section,on_delete= models.CASCADE)
    #StudentID = models.IntegerField('StudentID')
    StudentID = models.ForeignKey(Student, on_delete= models.CASCADE)
    ProfessorID = models.ForeignKey(Professor, on_delete= models.CASCADE)
    Review =  models.TextField(blank= True)
    Rating = models.IntegerField(blank=True)

    def __str__(self):
        return "Feedback for " + self.SectionID
    

#MCE Recommendations Quiz
class MCEQuestions(models.Model):
    questions_text = models.CharField(max_length=200)

class MCEAnswer(models.Model):
    question = models.ForeignKey(MCEQuestions, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)

class MCEUserResponse(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    answer = models.ForeignKey(MCEAnswer, on_delete=models.CASCADE)
    
class MCERecommendation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()