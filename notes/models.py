from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name="user",
        related_name="note",
        null=False,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, blank=True, default='Untitled')
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Note: {self.title} | created_at: {self.created_at}"
    