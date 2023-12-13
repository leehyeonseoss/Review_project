from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    # ///image = models.ImageField(upload_to='review_images/', blank=True, null=True)  # 추가
    
    
    def __str__(self):
        return self.subject
