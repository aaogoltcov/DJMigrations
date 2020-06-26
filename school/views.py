from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def data_prepare(students, teachers):
    for student in students:
        student['teachers'] = []
        for teacher in teachers:
            if teacher['students'] == student['id']:
                student['teachers'].append(dict(name=teacher['name'], subject=teacher['subject']))
    return students


def students_list(request):
    template = 'school/students_list.html'
    context = {
        'object_list': data_prepare(Student.objects.all().values().order_by('group'),
                                    Teacher.objects.prefetch_related('students').all().values('name',
                                                                                              'students',
                                                                                              'subject'))
    }
    return render(request, template, context)
