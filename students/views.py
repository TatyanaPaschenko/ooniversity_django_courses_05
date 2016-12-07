from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import StudentModelForm
from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)

        return qs


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/add.html'

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Student {0} has been successfully added.".format(
            self.object.name + ' ' + self.object.surname))
        return s

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/edit.html'

    def get_success_url(self):
        super().get_success_url()
        pk = self.kwargs['pk']
        return reverse('students:edit', args=(pk,))

    def form_valid(self, form):
        s = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return s


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/remove.html'

    def delete(self, request, *args, **kwargs):
        d = super().delete(request, *args, **kwargs)
        messages.success(request, "Info on {0} has been successfully deleted.".format(
            self.object.name + ' ' + self.object.surname))
        return d

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context


