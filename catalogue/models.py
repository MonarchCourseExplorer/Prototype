from django.db import models
from django.core.validators import MaxValueValidator
from users.models import Student, Professor

#MCE Standard Databases
class Department(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField('Course Name', max_length= 120)
    department = models.CharField(max_length=120) #department.abbreviation
    description = models.TextField(blank= True)
    number = models.CharField('Course Number',default='100', max_length=10) #probably excessive, but it doesn't hurt
    credits = models.CharField(max_length=10,default=3) #We aren't doing anything with this, so leave it as char so 1-3 works

    def __str__(self):
        return self.name

class Semester(models.Model):
    short_name = models.CharField('Abbreviated semester, i.e. 202410', max_length=50)
    friendly_name = models.CharField('Readable semester, i.e. Fall 2014', max_length=255)
    readonly = models.BooleanField()

    def __str__(self):
        return self.friendly_name
    
class Section(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    semester = models.CharField('Semester', max_length=50)
    session = models.CharField('Session', max_length=25)
    offering_time = models.CharField(default='00:00:00', max_length =255)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)
    delivery_type = models.CharField(max_length=255) 
    meeting_type = models.CharField(max_length=255)
    crn = models.IntegerField()

    def __str__(self):
        return f"{self.crn}"

class Syllabus(models.Model):
    section = models.ForeignKey(Section, on_delete = models.CASCADE)
    class_name = models.CharField('Course', default= 'name', max_length=50 )
    original_location = models.FileField(upload_to='documents/')
    #normalized_location = models.CharField('Normalized Location', max_length=120)
    
    def __str__(self):
        return f"{self.crn}"

#MCE Feedback
class Feedback(models.Model):
    #section_id = models.IntegerField('Course Number', blank=True) #CourseNumber
    section = models.ForeignKey(Section, on_delete= models.CASCADE)
    subject = models.CharField(max_length=255) #Subject
    semester = models.CharField(max_length=30) #Semester (i.e. Fall 2020)
    #professor_id = models.CharField('Professor Name', max_length=255) #Professor Name (Thomas Kennedy)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)
    review =  models.TextField(blank= True) #Share your thoughts
    difficulty_rating = models.IntegerField('Difficulty Rating', validators=[MaxValueValidator(5)]) 
    workload_rating = models.IntegerField('Workload Rating', validators=[MaxValueValidator(5)])
    openness_rating = models.IntegerField('Openness Rating', validators=[MaxValueValidator(5)])
    
    #Deleted Model Fields
    #StudentID = models.IntegerField('StudentID')
    #studentID = models.ForeignKey(Student, on_delete= models.CASCADE) #How will we incorporate this? 
    #professor_id = models.ForeignKey(Professor, on_delete= models.CASCADE) #Instructor
    #section_id = models.ForeignKey(Section, on_delete= models.CASCADE) #CourseNumber
    #rating = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.professor_id, self.subject, self.section_id}"

    

#MCE Recommendations Quiz

# class recquestions(models.Model):
#     questions_text = models.CharField(max_length=255)

# class recAnswer(models.Model):
#     question = models.ForeignKey(recquestions, on_delete=models.CASCADE)
#     choice = models.CharField(max_length=150)
    
# class MCERecommendation(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     course = models.CharField(max_length=15)
    
#     def __str__(self):
#         return self.title
    
# class recCombined(models.Model):
#     recommendation = models.OneToOneField(MCERecommendation, on_delete=models.CASCADE)
#     answer = models.ForeignKey(recAnswer, on_delete=models.CASCADE)
#     question = models.ForeignKey(recquestions, on_delete=models.CASCADE)