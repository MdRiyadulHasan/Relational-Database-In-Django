from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name = 'index_view'),
    path('delete/', views.deleteData, name = 'deleteData'),
    path('city/', views.CityInfo, name = 'CityInfo'),
    path('delete1/', views.DeleteCity, name = 'DeleteCity'),
]
