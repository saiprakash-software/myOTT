from django.db import models
from django.utils import timezone





class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# models.py

class DeletedVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deleted: {self.title}"
    
# models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    views = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



