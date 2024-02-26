from django.urls import path
from .views import ActList, ActDetail, EventDetail, EventList, ClubDetail , ClubList, DepartmentDetail
from .views import DepartmentList,SubjectList,SubjectDetail,TeacherDetail,TeacherList

app_name='isimm_api'

urlpatterns = [
    path('article/<int:pk>/', ActDetail.as_view(), name='detailcreate'),
    path("article/", ActList.as_view(), name='listcreate'),
    
    path('event/<int:pk>/', EventDetail.as_view(), name='detailcreate'),
    path("event/", EventList.as_view(), name='listcreate'),
    
    path('club/<int:pk>/', ClubDetail.as_view(), name='detailcreate'),
    path("club/", ClubList.as_view(), name='listcreate'),

     # Department endpoints
    path('department/', DepartmentList.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),

    # Teacher endpoints
    path('teacher/', TeacherList.as_view(), name='teacher-list'),
    path('teacher/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),                  

    # Subject endpoints
    path('subject/', SubjectList.as_view(), name='subject-list'),
    path('subject/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),

    #path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    #path('department/', DepartmentList.as_view(), name='department-list'),

    #path('enseignant/<int:pk>/', EnseignantDetail.as_view(), name='enseignant-detail'),
    #path('enseignant/', EnseignantList.as_view(), name='enseignant-list'),

    #path('formation/<int:pk>/', FormationDetail.as_view(), name='formation-detail'),
    #path('formation/', FormationList.as_view(), name='formation-list'),

    #path('matiere/<int:pk>/', MatiereDetail.as_view(), name='matiere-detail'),
    #path('matiere/', MatiereList.as_view(), name='matiere-list'),

    
]