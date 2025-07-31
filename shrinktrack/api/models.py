from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
class ShrinkInstanceModel(models.Model):
    id = models.UUIDField(default=uuid4,primary_key=True,blank=False,editable=False,unique=True)
    user = models.ForeignKey(User,related_name='urls',on_delete=models.CASCADE)
    original_url = models.URLField(blank=False,editable=True,unique=True)
    shrinked_url = models.URLField(blank=False,editable=False,unique=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)