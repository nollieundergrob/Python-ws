from django.db import models
import datetime
class ChatMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_user = models.CharField(max_length=100,default='0.0.0.0')
    date = models.CharField(default=datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))