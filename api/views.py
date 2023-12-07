from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin
# Create your views here.

class StudentList(ListModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializers

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrive(RetrieveModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)