from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import HttpResponseRedirect




def allblogs(request):
    blogs = Blog.objects
    return render(request, 'allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': detailblog})


def comment(request):
    hel = request.POST['message']
    return render(request, 'detail.html', {'questions': hel})

