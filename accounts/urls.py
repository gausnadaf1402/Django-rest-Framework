from django.urls import path,include
from . import views
urlpatterns = [
    # path('cls_list/',views.cls_list,name='classroom_list'),
    # path('cls_detail/<int:pk>/',views.cls_detail,name='classroom_detail')
    path('cls_list/',views.ClsListView.as_view()),
    path('cls_create/',views.ClsCreateView.as_view()),
    path('cls_detail/<int:pk>/',views.clsDetailView.as_view()),
    path('stu_list/',views.StuListView.as_view()),
    path('stu_create/',views.StuCreateView.as_view()),
    path('stu_detail/<int:pk>/',views.StuDetailView.as_view()),
    path('sub_list/',views.SubListView.as_view()),
    path('sub_create/',views.SubCreateView.as_view()),
    path('sub_detail/<int:pk>/',views.SubDetailView.as_view()),
    path('teach_list/',views.TeachListView.as_view()),
    path('teach_create/',views.TeachCreateView.as_view()),
    path('teach_detail/<int:pk>/',views.TeachDetailView.as_view()),
    path('leave_list/',views.LeaveListView.as_view()),
    path('leave_create/',views.LeaveCreateView.as_view()),
    path('leave_detail/<int:pk>/',views.LeaveDetailView.as_view())
]
