from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from isimm.models import Article, Club #, Matiere, Department, Enseignant, Formation'''
from .serializers import ArticleSerializer, ClubSerializer#, DepartmentSerializer, EnseignantSerializer, FormationSerializer, MatiereSerializer
from isimm.models import Department, Subject, Teacher
from .serializers import DepartmentSerializer, SubjectSerializer,TeacherSerializer
from rest_framework.permissions import SAFE_METHODS,  BasePermission, IsAdminUser , DjangoModelPermissionsOrAnonReadOnly
# Create your views here.

class PostUserWritePermission(BasePermission):
    message = 'editing posts is restricted to the author only'

    # it called object bc we instance of user we are cheking
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS: #Safe methode for read only 
            return True
        
        return obj.author == request.user #he can do update and add

        

class ActList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ActDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class EventList(generics.ListAPIView):
    queryset = Article.eventObject.all()
    serializer_class = ArticleSerializer

class EventDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.eventObject.all()
    serializer_class = ArticleSerializer

class ClubList(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


# Department Views
class DepartmentList(generics.ListCreateAPIView):
    """
    List and create departments.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a department.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# Teacher Views
class TeacherList(generics.ListCreateAPIView):
    """
    List and create teachers.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Modify response to include department name
        for item in data:
            department_id = item.get('department')
            department = Department.objects.filter(id=department_id).first()
            if department:
                item['department_name'] = department.name
            else:
                item['department_name'] = None

        return Response(data)

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a teacher.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# Subject Views
class SubjectList(generics.ListCreateAPIView):
    """
    List and create subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a subject.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class ClubDetail(generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
