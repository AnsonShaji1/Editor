from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    topic = models.TextField()
    var1 = models.TextField()
    sub_topic = models.TextField()
    var2=models.TextField()
    short=models.TextField()
    possible=models.TextField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    image=models.TextField()
    ck=RichTextField()
    def __str__(self):
        return self.topic