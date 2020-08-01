from django.db import models
import os
# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=200)
    year = models.IntegerField()
    school = models.CharField(max_length = 300)
    result = models.CharField(max_length=100)
    description = models.TextField()

class Experience(models.Model):
    title = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    duration = models.CharField(max_length = 100)
    technology = models.CharField(max_length=400)
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FilePathField(path='resume\static\media')
    link = models.URLField(default='https://github.com/bhavnas23')

    @property
    def imgPath(self):
        # return os.path.join(os.getcwd(),'resume')
        return self.image.replace('resume', '')

class Achievement(models.Model):
    description = models.TextField()

class Skill(models.Model):
    skill = models.CharField(max_length = 100)
    rating = models.IntegerField()

    @property
    def calPer(self):
        return self.rating*10