from django.urls import path
from .views import student_list, student_detail, student_new, student_edit, student_delete, category_students

urlpatterns = [
    path('', student_list, name='student_list'),
    path('student/<int:pk>/', student_detail, name='student_detail'),
    path('student/new/', student_new, name='student_new'),
    path('student/<int:pk>/edit/', student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', student_delete, name='student_delete'),
    path('category/<str:category_name>/', category_students, name='category_students'),
]
