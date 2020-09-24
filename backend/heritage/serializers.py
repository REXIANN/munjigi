from rest_framework import serializers
from .models import Heritage
from review.serializers import ReviewSerializer


# 문화재 리스트 

class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ('__all__')


class HeritageDetailSerializer(serializers.ModelSerializer):
    heritage_reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Heritage
        fields = ('__all__')

