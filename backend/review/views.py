from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import ReviewSerializer
from .models import Review


class ReviewListAPI(generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(many=True)
        pagination_class = PageNumberPagination
        return Response(serializer.data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPI(generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, pk):
        queryset = get_object_or_404(Review, pk=pk)
        serializer = self.get_serializer()
        return Response(serializer.data)
    

    def put(self, request, pk):
        queryset = get_object_or_404(Review, pk=pk)
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        queryset = get_object_or_404(Review, pk=pk)
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        