

from django.urls import path
from . import views

urlpatterns = [

     path('',views.front_view,name='front_page'),
     # path('login/',views.login_view,name='login'),
     # path('register/',views.register_view,name='register'),
     path('about/',views.about_view,name='about'),

]
