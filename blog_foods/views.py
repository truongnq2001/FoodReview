from django.contrib.auth import forms
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

import blog_foods
from .models import Post, User, Profile, UpProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.files.images import get_image_dimensions
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
import datetime
import random
# Create your views here.

def index(request):
    """Show all Post."""
    posts = Post.objects.all()
    up = UpProfile.objects.all()
    if UpProfile.objects.filter(user_id=request.user.id).exists():
        UpdateProfile = get_object_or_404(UpProfile, user_id=request.user.id)
        Temp = 1
        rd = 1
        return render(request, 'index.html', {'posts': posts, 'UpdateProfile': UpdateProfile, 'Temp':Temp, 'up':up, 'rd':rd})
    else:
        Temp = 0
        return render(request, 'index.html', {'posts': posts, 'Temp':Temp, 'up':up})

def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        image.name = str(datetime.datetime.now()) + ".png";
        address = request.POST.get("address")
        description = request.POST.get("description")
        summary = request.POST.get('summary')
        caption = request.POST.get('caption')
        price = request.POST.get('price')
        rate = request.POST.get('rate')
        user = request.user.username
        posted_by = request.user
        new_post = Post.objects.create(address = address , summary=summary,price = price, image = image, caption = caption , description = description, rate = rate,user =user, posted_by = posted_by)
        new_post.save()
    
    return redirect('/')

def register(request):
    form = UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            if regForm.save():
                img = "image_user/e56154546cf4be74e393c62d1ae9f9d4.jpg"
                summary_user = "Đây là tài khoản thuộc hệ thống PTIT FOOD"
                Facebook = ""
                Instagram = ""
                owner = User.objects.all().order_by("-id")[0]
                new_profile = UpProfile.objects.create(user=owner, Facebook = Facebook, Instagram = Instagram, summary_user = summary_user, image_user=img )
                new_profile.save()
            messages.success(request,'User has been regiserted.')
            return redirect('login')
    return render(request,'registration/register.html',{'form':form})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    num = Post.objects.get(id=pk).posted_by_id
    up = UpProfile.objects.all()
    if UpProfile.objects.filter(user_id=num).exists():
        UpdateProfile = get_object_or_404(UpProfile, user_id=num)
        Temp = 1
        return render(request, 'post.html', {'UpdateProfile': UpdateProfile, 'Temp':Temp, 'post' : post, 'up': up})
    else:
        Temp = 0
        return render(request, 'post.html', {'Temp':Temp, 'post' : post, 'up': up})

def author(request, id):
    singleAuthor = get_object_or_404(User, id=id)
    postss = Post.objects.filter(posted_by_id=id)
    if UpProfile.objects.filter(user_id=id).exists():
        UpdateProfile = get_object_or_404(UpProfile, user_id=id)
        Temp = 1
        return render(request, 'author.html', {'singleAuthor': singleAuthor, 'postss': postss, 'UpdateProfile': UpdateProfile, 'Temp':Temp})
    else:
        Temp = 0
        return render(request, 'author.html', {'singleAuthor': singleAuthor, 'postss': postss, 'Temp':Temp})
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['up'] = UpProfile.objects.all()
        return context 

def profile(request):
    if UpProfile.objects.filter(user_id=request.user.id).exists():
        UpdateProfile = get_object_or_404(UpProfile, user_id=request.user.id)
        Temp = 1
        return render(request, 'profile.html', {'UpdateProfile': UpdateProfile, 'Temp':Temp})
    else:
        Temp = 0
        return render(request, 'profile.html', {'Temp':Temp})

def upload_profile(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        if img == True:
            width, height = get_image_dimensions(img)
            if width >= 400 or height >= 400:
                return redirect('/profile/')
        if len(request.FILES) is 0:
            img = UpProfile.objects.get(user_id=request.user.id).image_user 
        summary_user = request.POST.get('summary_user')
        name_user = request.POST.get('name_user')
        Facebook = request.POST.get('Facebook')
        Instagram = request.POST.get('Instagram')
        owner = request.user
        if name_user == request.user.username:
            owner.save()
            UpProfile.objects.filter(user=request.user).delete() 
            if  summary_user == '':
                summary_user = "Đây là tài khoản thuộc hệ thống PTIT FOOD"
            new_profile = UpProfile.objects.create(user=owner, Facebook = Facebook, Instagram = Instagram, summary_user = summary_user, image_user=img )
            new_profile.save()
            return redirect('/author/%i' % request.user.id)
        owner.username = name_user
        user_model = get_user_model()
        if  user_model.objects.filter(username=owner.username):
            messages.success(request, 'Tên đã được sử dụng, vui lòng nhập lại!')
            return redirect('/profile/')
        owner.save()
        UpProfile.objects.filter(user=request.user).delete() 
        if  summary_user == '':
            summary_user = "Đây là tài khoản thuộc hệ thống PTIT FOOD"
        new_profile = UpProfile.objects.create(user=owner, Facebook = Facebook, Instagram = Instagram, summary_user = summary_user, image_user=img )
        new_profile.save()

    return redirect('/author/%i' % request.user.id)
class UpdatePostView(UpdateView):
    model =Post
    template_name = 'update_post.html'
    form_class = UpdateForm
    success_url = reverse_lazy('blog_foods:index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['up'] = UpProfile.objects.all()
        return context 
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog_foods:index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['up'] = UpProfile.objects.all()
        return context 

