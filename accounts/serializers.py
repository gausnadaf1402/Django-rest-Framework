from rest_framework import serializers
from .models import Classroom,Student,Subject,Teacher,Leave,Attendance

class ClassroomSerializer(serializers.ModelSerializer):
    # students=StudentSerializer(many=True)
    class Meta:
        model=Classroom
        fields='__all__'


class SubjectSerializer(serializers.ModelSerializer):
    # teachers=TeacherSerializer(many=True)
    class Meta:
        model=Subject
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    subjects=SubjectSerializer(many=True)#inline serializer
    class Meta:
        model=Teacher
        fields='__all__'


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields='__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    # current_class=ClassroomSerializer()# inline serializer
    leaves=LeaveSerializer(many=True)
    class Meta:
        model=Student
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'



