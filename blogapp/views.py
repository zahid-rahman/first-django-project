from django.shortcuts import render
from .models import Post


# Create your views here.


def front_view(request):
    all_post = Post.objects.all()
    context = {
        'all_post': all_post
    }
    return render(request, 'index.html', context)


# def login_view(request):
#     return render(request,'auth/login.html',{'title':'Login'})


def about_view(request):
    return render(request, 'about/about.html', {'title': 'About'})
