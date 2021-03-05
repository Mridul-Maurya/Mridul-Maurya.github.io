from django.urls import path
from . import views 
urlpatterns = [
   path('', views.index, name='index'),
   path('courses/', views.courses, name='courses'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('subjects/', views.subjects, name='subjects'),
   path('course/<int:course_id>', views.coursedetail, name='coursedetail'),
   path('snippet/', views.snippet_detail, name='snippet_detail'),
]