from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('profile/', user_views.profile_view, name='profile'),
    path('register/', user_views.register_view, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    path('upload_post/', user_views.upload_post_view, name='upload.post.page'),
    path('user_post/<int:id>', user_views.view_user_post, name='user.post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
