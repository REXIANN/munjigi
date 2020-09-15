from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import HeritageSerializer
from .models import Heritage


class HeritageListAPI(generics.GenericAPIView):
    def get(self, request):
        heritages = Heritage.objects.all()
        serializer_class = HeritageSerializer
        pagination_class = PageNumberPagination
        return Response(heritages)
    

