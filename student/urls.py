from django.urls import path
from . import views

urlpatterns = [
    path('filier/', views.FilierList.as_view()),
    path('filier/<int:pk>', views.FilierDetail.as_view()),
    path('student/', views.StudentsList.as_view()),
    path('student/<int:pk>', views.StudentsDetail.as_view()),
]