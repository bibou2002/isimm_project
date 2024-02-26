from rest_framework import serializers
from isimm.models import Article, Club,Department ,Subject,Teacher

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'qualification', 'joining_date', 'contact_details', 'department']
    
    

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all_'