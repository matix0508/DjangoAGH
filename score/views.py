from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Subject

# Create your views here.


def index(request):
    return HttpResponse("Hello, world")


def subjects(request):
    subject_lst = Subject.objects.all()
    context = {
        'lst': subject_lst
    }
    return render(request, 'score/index.html', context)


def subject(request, subject_id):
    subject_item = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'score/detail.html', {'subject': subject_item})


def new_subject(request):
    pass

