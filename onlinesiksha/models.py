from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pub_date =models.DateTimeField(auto_now=False, auto_now_add=False)
    teacher =  models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    discription = models.TextField(max_length=2000, help_text='Enter a brief description of the course')
    syllabus = models.TextField(max_length=2000)
    course_file =  models.FileField(upload_to='files/', max_length=100,blank=True)
    subject = models.ManyToManyField('Subject', help_text='Select a subject for this course')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
          """Returns the url to access a particular author instance."""
          return reverse('course-detail', args=[str(self.id)])
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    teacher_image = models.ImageField(upload_to='images/')
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    subjects = models.ManyToManyField('Subject', help_text='Select a subject for this teacher')
    body = models.TextField(max_length=1000)
    def __str__(self):
        pass
        return f'{self.last_name}, {self.first_name}'
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('teacher-detail', args=[str(self.id)])
        
class Subject(models.Model):
    title = models.CharField(max_length=100)
    #date= models.DateField(auto_now=False,auto_now_add=False)
    subject_image = models.ImageField(upload_to='images/')
    subject_body = models.TextField(max_length=1000)
    subject_file =  models.FileField(upload_to='files/%Y/%m/%d/', max_length=100)
     
    class Meta:
        ordering = ["title"]
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('subject-detail', args=[str(self.id)])


class Snippet(models.Model):
    """docstring for Snippet"""
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name

     
        