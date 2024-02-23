from django.urls import path
from django.views.generic import TemplateView

app_name='isimm'

urlpatterns = [
    
    path("",TemplateView.as_view(template_name="isimm/index.html"))
]