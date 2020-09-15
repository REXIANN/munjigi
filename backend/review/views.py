from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import ReviewSerializer
from .models import Review


class ReviewListAPI(generics.GenericAPIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        pagination_class = PageNumberPagination
        return Response(serializer.data)
    

