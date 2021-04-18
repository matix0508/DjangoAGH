from django.urls import path

from . import views

app_name = 'score'
urlpatterns = [
    path('', views.subjects, name='subjects'),
    path('new/', views.new_subject, name='new_subject'),
    path('<int:subject_id>/', views.subject, name='subject')
]
