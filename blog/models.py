from django.db import models
from embed_video.fields import EmbedVideoField
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Blog(models.Model):
    Blogger = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    # description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
