from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import News, NewsTypes
from .serializers import NewSerializer, NewTypeSerializer


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewSerializer


class NewTypeViewSets(viewsets.ModelViewSet):
    queryset = NewsTypes.objects.all()
    serializer_class = NewTypeSerializer


class GetNews(APIView):
    def get(self, request, *args, **kwargs):
        index = kwargs.get("pk")
        if NewsTypes.objects.filter(pk=index):
            item = NewsTypes.objects.get(pk=index)
            lst = item.get_news.all().values()
            return Response({"news": lst})
        return Response("There is no such new")


class AllNews(APIView):
    def get(self, request):
        lst = News.objects.select_related("new_type").values('title', 'short_description','new_type__name', 'new_type__colour')
        return Response({"news": lst})
