from django.shortcuts import render

# Create your views here.


def front_view(request):
    return render(request,'index.html')

# def login_view(request):
#     return render(request,'auth/login.html',{'title':'Login'})



def about_view(request):
    return render(request,'about/about.html',{'title':'About'})
