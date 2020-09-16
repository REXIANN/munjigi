from rest_framework import generics
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import HeritageSerializer, HeritageDetailSerializer
from .models import Heritage
from backend.pagination import CustomPagination


class HeritageListAPI(GenericAPIView):
    serializer_class = HeritageSerializer
    queryset = Heritage.objects.all()
    pagination_class = CustomPagination
    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)

# class HeritageListAPI(generics.GenericAPIView):
#     queryset = Heritage.objects.all()
#     serializer_class = HeritageSerializer
#     pagination_class = PageNumberPagination
#     def get(self, request):
#         heritages = Heritage.objects.all()
#         serializer = HeritageSerializer(heritages, many=True)
#         return Response(serializer.data)


class HeritageDetailAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer
    def get(self ,request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        serializer = HeritageDetailSerializer(heritage)
        return Response(serializer.data)