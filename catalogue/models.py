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
    number = models.CharField('Course Number',default='100', max_length=10) #probably excessive, but it doesn't hurt
    credits = models.CharField(max_length=10,default=3) #We aren't doing anything with this, so leave it as char so 1-3 works

    def __str__(self):
        return self.name
    
class Section(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    #courseID = models.IntegerField() #is this the CRN?
    semester = models.CharField('Semester', max_length=50)
    session = models.CharField('Session', max_length=25)
    offering_time = models.CharField(default='00:00:00', max_length =255) # models.TimeField(auto_now=False, auto_now_add=False)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)
    delivery_type = models.CharField(max_length=25)
    meeting_type = models.CharField(max_length=25)
    crn = models.IntegerField()

    def __str__(self):
        return self.course + " " + self.professor.first_name + " " + self.professor.last_name

class Syllabus(models.Model):
    #SectionID = models.ForeignKey(Section,on_delete= models.CASCADE)
    class_name =models.CharField('Course',default= 'name',max_length=50 )
    OriginalLocation = models.FileField(upload_to='documents/')
    NormalizedLocation = models.CharField('Normalized Location', max_length=120)
    

    def __str__(self):
        #return  "Syllabus for " + self.SectionID
        return  "Syllabus for " + self.class_name

#MCE Feedback
class Feedback(models.Model):
    SectionID = models.ForeignKey(Section,on_delete= models.CASCADE) #CourseNumber
    Subject = models.TextField(blank= True) #Subject for course RECENTLY ADDED
    Semester = models.TextField(blank= True) #semester of section RECENTLY ADDED
    #StudentID = models.IntegerField('StudentID')
    StudentID = models.ForeignKey(Student, on_delete= models.CASCADE) #How will we incorporate this? 
    ProfessorID = models.ForeignKey(Professor, on_delete= models.CASCADE) #Instructor
    Review =  models.TextField(blank= True) #Share your thoughts
    Rating = models.IntegerField(blank=True) #Group must add this on front end -- still need a rating averager

    def __str__(self):
        return "Feedback for " + self.SectionID
    
    

#MCE Recommendations Quiz
class recQuestions(models.Model):
    questions_text = models.CharField(max_length=255)

class recAnswer(models.Model):
    question = models.ForeignKey(recQuestions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=150)
    
class MCERecommendation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title
    
    #