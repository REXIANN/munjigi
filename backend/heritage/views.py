from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import HeritageSerializer, HeritageDetailSerializer
from .models import Heritage


class HeritageListAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer
    def get(self, request):
        heritages = Heritage.objects.all()
        serializer = HeritageSerializer(heritages, many=True)
        pagination_class = PageNumberPagination
        return Response(serializer.data)


class HeritageDetailAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer
    def get(self ,request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        serializer = HeritageDetailSerializer(heritage)
        return Response(serializer.data)