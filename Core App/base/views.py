from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
class StudentAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    lookup_field='id'
    def get(self,request):
         return self.list(request)
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    def post(self,request):
       return self.create(request)
    def put(self,request,id=None):
        return self.update(request,id)
    def delete(self,request,id=None):
        return self.destroy(request,id)
    

