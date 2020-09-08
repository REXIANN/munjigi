from django.db import models
from django.conf import settings

class Heritage(models.Model):
    selnum = models.IntegerField(primary_key=True)
    k_name = models.CharField(max_length=50)
    h_name = models.CharField(max_length=50)
    content = models.TextField()
    imageURL = models.URLField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    era = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150)
    clsfc_code = models.IntegerField()
    clsfc_name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_heritages', blank=True)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    heritage = models.ForeignKey(Heritage, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_recommend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="recommend_reviews", blank=True)