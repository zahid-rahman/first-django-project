from django.http import HttpResponse

def homeView(request):
    return HttpResponse('hello world')

 
