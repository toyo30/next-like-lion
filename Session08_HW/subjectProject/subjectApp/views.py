from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView, View
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm 
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm 
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')





def koreanSubjectView(request):
    subjects = Subject.objects.all()
    koreanMajor = subjects.filter(major_id='1')
    return render(request, 'korean.html', {
        'koreanMajor': koreanMajor,
    })


def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major_id='2')
    return render(request, 'computer.html', {
        'computerMajor': computerMajor,
    })


def start(request):
    return render(request, 'start.html')


def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {
        'majors':majors,
        'subjects':subjects,
        })

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

