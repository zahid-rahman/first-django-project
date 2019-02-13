from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm , UserUpdateForm, ProfileUpdateForm,UserPostForm
from django.contrib.auth.decorators import login_required
from blogapp.models import Post
# from blogapp.models import Catgeory



# Create your views here.

def register_view(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created now you are able to login')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request,'auth/register.html',{'form':form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your accont has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'user/profile.html',context)


def upload_post_view(request):

    if request.method == 'POST':
        ps_form = UserPostForm(request.POST)
        # ps_form.fields['author_id'].initial = str(request.user.id)
        # ps_form.fields['content'].initial = 'hello'

        if ps_form.is_valid():

            ps_form.save()
            messages.success(request, f'Your post uploaded successfully')

            return redirect('profile')

    else:
        # ps_form = UserPostForm(initial={"author": request.user.username})

        ps_form = UserPostForm()
        ps_form.fields['category_name'].initial = Catgeory.objects.all()


    context = {
        'ps_form':ps_form
    }

    return render(request,'user/upload_post.html',context);


def view_user_post(request,id):

    user_post = Post.objects.filter(author_id=id)
    context={
        'user_post':user_post
    }


    return render(request,'posts/post.html',context)


def delete_user_post(request,id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()

    return redirect('user.post', id)

