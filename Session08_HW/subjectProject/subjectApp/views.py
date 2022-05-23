from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
import pdb

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


class ListMajorView(ListView):
    model = Major
    template_name = 'major_page.html'

    def get_context_data(self, **kwargs):
        context = super(ListMajorView, self).get_context_data()
        context['subjects'] = Subject.objects.all()

        return context


class SubjectListView(ListView):
    model = Subject
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectListView, self).get_context_data()
        context['majors'] = Subject.objects.all()

        return context

def major_page(request, major_name):

    subjects = Subject.objects.all()
    major = Major.objects.get(name=major_name)
    # print(major)
    # print('안녕하세요')
    # print(Subject.objects.filter(major=major))
    # pdb.set_trace()
  
    return render(
        request,
        'major_page.html',
        {
        'subjects': subjects,
        'subject_list': Subject.objects.filter(major=major),
        'majors': Major.objects.all(),
        'major': major,
        }
    )


def koreanSubjectView(request):
    # computer/?major=english
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

def add(request):
    return render(request, 'add.html')


def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {
        'majors':majors,
        'subjects':subjects,
        })

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    # print('안녕하세요')
    # print(delMajor)
    # pdb.set_trace()
    delMajor.delete()
    return redirect('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

