from django.urls import path
from . import views

urlpatterns = [

     path('',views.front_view,name='front_page'),
     path('about/',views.about_view,name='about'),
     path('user_post/<int:id>',views.user_post,name='user.post'),

]