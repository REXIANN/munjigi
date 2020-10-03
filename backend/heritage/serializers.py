from rest_framework import serializers
from .models import Heritage, Tag
from review.serializers import ReviewListSerializer


# 문화재 리스트 

class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ('__all__')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')


class HeritageDetailSerializer(serializers.ModelSerializer):
    heritage_reviews = ReviewListSerializer(many=True, read_only=True)
    heritage_tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Heritage
        fields = ('__all__')


