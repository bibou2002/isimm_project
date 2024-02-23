from django.shortcuts import render
from rest_framework import generics
from isimm.models import Article, Club #, Matiere, Department, Enseignant, Formation'''
from .serializers import ArticleSerializer, ClubSerializer#, DepartmentSerializer, EnseignantSerializer, FormationSerializer, MatiereSerializer
from isimm.models import Department, Teacher, Subject
from .serializers import DepartmentSerializer, TeacherSerializer, SubjectSerializer

# Create your views here.

class ActList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ActDetail(generics.RetrieveDestroyAPIView):
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


'''class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EnseignantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class EnseignantList(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class FormationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

class FormationList(generics.ListCreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

class MatiereDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer

class MatiereList(generics.ListCreateAPIView):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer
    
'''
class ClubDetail(generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
