from django.urls import path

from . import views

app_name = 'score'
urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subjects/new/', views.SubjectFormView.as_view(), name='new_subject'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject'),
    path('fields/', views.FieldListView.as_view(), name='fields'),
    path('fields/new/', views.FieldFormView.as_view(), name='new_field'),
    path('fields/<int:pk>/', views.FieldDetailView.as_view(), name='field')
]
