from django.shortcuts import render, redirect, HttpResponse
from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import CourseForm, CommentForm
from .models import Course, Comment


def index(request):
    courses = Course.objects.all()
    if request.method == 'GET':
        return render(request, 'course_app/index.html', { 'form' : CourseForm(), 'courses' : courses })
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            errors = Course.objects.validate(request.POST)
            if errors:
                for tag, error in errors.iteritems():
                    messages.error(request, error)
                return render(request, 'course_app/index.html', { 'form' : form, 'courses' : courses })
            else:
                form.save()                               
                return redirect(reverse('courses:index'))
        else:
            return render(request, 'course_app/index.html', { 'form' : form, 'courses' : courses })                            
                     


def show(request, id):
    return render(request, 'course_app/show.html', { 'course' : Course.objects.get(id=id), 'form' : CommentForm()})


def comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = Course.objects.get(id=id)
            comment.save()
    return redirect(reverse('courses:show', kwargs={'id': id}))            
                

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('courses:index'))
