from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string

from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by("-date")
    return render(request, 'blogs/list.html', {'blogs':blogs})

def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog_detail})
