from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import HeritageSerializer
from .models import Heritage


class HeritageListAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(many=True)
        pagination_class = PageNumberPagination
        return Response(serializer.data)