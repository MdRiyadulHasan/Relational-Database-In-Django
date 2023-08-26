from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name = 'index_view'),
    path('delete/', views.deleteData, name = 'deleteData'),
    path('city/', views.CityInfo, name = 'CityInfo'),
    path('delete1/', views.DeleteCity, name = 'DeleteCity'),
    path('course/', views.CourseView, name = 'CourseView'),
    path('course1/', views.course_list, name = 'course_list'),
    path('student/', views.student_view, name = 'student_view'),
]
