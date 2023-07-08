from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Classroom,Student,Subject,Teacher,Leave
from .serializers import ClassroomSerializer,StudentSerializer,SubjectSerializer,TeacherSerializer,LeaveSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


# Create your views here.
                    #####Class based view#####

class ClsListView(APIView):
    def get(self,request):
        classroom=Classroom.objects.all()
        serializer=ClassroomSerializer(classroom,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ClsCreateView(APIView):
    def post(self,request):
        serializer=ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class clsDetailView(APIView):
    def get_object(self,pk):
        try:
            return Classroom.objects.get(pk=pk)
        except Classroom.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        classroom=self.get_object(pk)
        serializer=ClassroomSerializer(classroom)
        return Response(serializer.data)
    def put(self,request,pk):
        classroom=self.get_object(pk)
        serializer=ClassroomSerializer(classroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        classroom=self.get_object(pk)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StuListView(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class StuCreateView(APIView):
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class StuDetailView(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        student=self.get_object(pk)
        leaves=Leave.objects.filter(student_id=13)
        leave_serializer = LeaveSerializer(leaves, many=True)
        # serializer=StudentSerializer(student)
        return Response(leave_serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        student=self.get_object(pk)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubListView(APIView):
    def get(self,request):
        subject=Subject.objects.all()
        serializer=SubjectSerializer(subject,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SubCreateView(APIView):
    def post(self,request):
        serializer=SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class SubDetailView(APIView):
    def get_object(self,pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        subject=self.get_object(pk)
        serializer=SubjectSerializer(subject)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        subject=self.get_object(pk)
        serializer=SubjectSerializer(subject,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        subject=self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeachListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TeachCreateView(APIView):
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class TeachDetailView(APIView):
    def get_object(self,pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        teacher=self.get_object(pk)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        teacher=self.get_object(pk)
        serializer=TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        teacher=self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LeaveListView(APIView):
    def get(self,request):
        leave=Leave.objects.all()
        serializer=LeaveSerializer(leave,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class LeaveCreateView(APIView):
    def post(self,request):
        serializer=LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class LeaveDetailView(APIView):
    def get_object(self,pk):
        try:
            return Leave.objects.get(pk=pk)
        except Leave.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        leave=self.get_object(pk)
        serializer=LeaveSerializer(leave)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        leave=self.get_object(pk)
        serializer=LeaveSerializer(leave,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        leave=self.get_object(pk)
        leave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


















             ##### Function based view #####
# @api_view(['GET','POST'])
# def cls_list(request):
#     if request.method=='GET':
#         classroom=Classroom.objects.all()
#         serializer=ClassroomSerializer(classroom,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=ClassroomSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def cls_detail(request,pk):
#     try:
#         classroom=Classroom.objects.get(pk=pk)
#     except Classroom.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#         serializer=ClassroomSerializer(classroom)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=='PUT':
#         data=JSONParser().parse(request)
#         serializer=ClassroomSerializer(classroom,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='DELETE':
#         classroom.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


