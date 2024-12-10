from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    media = models.FileField(upload_to='uploads/', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.media_type.capitalize()} Post"

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
