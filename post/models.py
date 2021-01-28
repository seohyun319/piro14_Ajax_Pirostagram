from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subject/')
    content = models.TextField()
    like = models.BooleanField(default=False)

class Comment(models.Model):
    subject = models.ForeignKey("Subject", related_name = "comments" ,on_delete=models.CASCADE, blank=True, default=None)
    comment = models.CharField(max_length=100, blank=True)