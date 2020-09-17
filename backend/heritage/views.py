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
        if request.session.get("h_hit", False) == False:
            request.session["h_hit"] = []
        hit_l = request.session["h_hit"]
        if pk not in hit_l:
            hit_l.append(pk)
            request.session["h_hit"] = hit_l
            print(hit_l)
            heritage.hit += 1
        
        h_data = HeritageDetailSerializer(heritage).data
        serializer = HeritageDetailSerializer(heritage, data = h_data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        print("띠용")

        return Response(serializer.data)