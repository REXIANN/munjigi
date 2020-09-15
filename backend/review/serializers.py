from rest_framework import serializers
from .models import Review


# 리뷰 리스트

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')
