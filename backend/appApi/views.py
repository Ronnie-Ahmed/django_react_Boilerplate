from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializers
from rest_framework import generics
from rest_framework import status

# Create your views here.

class UserView(APIView):
    def get(self,request,*args,**kwargs):
        user=User.objects.all()
        serializers=UserSerializers(user,many=True)
        return Response(serializers.data)
    
    def post(self,request,*args,**kwargs):
        serializers=UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class SingleUserView(APIView):
    def get_object(self,request,pk,*args,**kwargs):
        try:
            user=User.objects.get(pk=pk)
            return user
        except :
            Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk,*args,**kwargs):
        user=self.get_object(pk)
        serializers=UserSerializers(user).data
        return Response(serializers.data)
    
    # def post(self,request,pk,*args,**kwargs):
    #     serializers=UserSerializers(data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response(serializers.errors)
    
    def put(self,request,pk,*args,**kwargs):
        user=self.get_object(pk)
        serializers=UserSerializers(user,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
        
        
        
    
class GetUserView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    
class PostUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    
class GetSingleUserView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    
