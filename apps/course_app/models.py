from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name must be more than 5 characters'
        if len(postData['description']) < 15:
            errors['description'] = 'Course description must be more than 15 characters'
        return errors


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    course = models.ForeignKey(Course, related_name = 'comments', on_delete = models.CASCADE)       
    
    
