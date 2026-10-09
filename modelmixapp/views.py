from django.shortcuts import render
from modelmixapp.models import status
from modelmixapp.serializer import StatusSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import mixins
# Create your views here.

class AllStatusAddView(ListAPIView,mixins.CreateModelMixin):
    queryset = status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request,*args, **kwargs):
        return self.create(request, *args, **self.kwargs)

class StatusRetriveUpdateDeleteView(RetrieveAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = status.objects.all()
    serializer_class = StatusSerializer


    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **self.kwargs)


    def delete(self ,request, *args, **kwargs):
        return self.destroy(request,*args, **self.kwargs)