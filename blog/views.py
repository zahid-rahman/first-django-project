

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm , UserUpdateForm, ProfileUpdateForm,UserPostForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def front_view(request):
    return render(request,'index.html')

# def login_view(request):
#     return render(request,'auth/login.html',{'title':'Login'})



def about_view(request):
    return render(request, 'about/about.html', {'title': 'About'})
    


def register_view(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #create profile
            user_id = User.objects.values_list('id',flat=True).last()
            create_profile = Profile(image="default.jpg",user_id=user_id)
            create_profile.save()

            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created now you are able to login')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form':form
    }
    return render(request,'auth/register.html',context)


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
        ps_form = UserPostForm(request.POST,instance=request.user.username)
        if ps_form.is_valid():
            ps_form.save()



            # author_name = request.user.username
            #
            # new_submit = ps_form.save(commit=False)
            # new_submit.author = author_name
            # new_submit.save()
            messages.success(request, f'Your post uploaded successfully')

            return redirect('profile')

    else:
        ps_form = UserPostForm()

    context = {
        'ps_form':ps_form
    }

    return render(request,'user/upload_post.html',context);