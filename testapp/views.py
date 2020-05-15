from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer,UserSerializer
from django.shortcuts import render, redirect
# Create your views here.

# User Details API View
class UserDetailView(APIView):
    def get(self,request,id):
        register=Profile.objects.get(id=id)
        serializer=UserSerializer(register)
        return Response(serializer.data)

# Classes List grade 1-12 API
class ProductListView(APIView):

    def get(self,request):
        products=Posts.objects.all()
        serializer=ProductSerializer(products,many=True)

        return Response(serializer.data)
    def post(self,request):
        serializer=ProductSerializer(data=request)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Classes Task details API View
class ProductDetailView(APIView):
    def get(self,request,id):
        product=Posts.objects.get(id=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

# Classes List 1-12
def post_list(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
        }
    return render(request, 'index.html', context)
# Classes Task Detail and login is required to enter in classes task
@login_required(login_url="user_login")
def post_detail(request, id):
    post = Posts.objects.get( id=id)
    context = {
        'post': post,
            }
    return render(request, 'post_detail.html', context)

# User Login page
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

# User Signup
def signup_view(request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.board = form.cleaned_data.get('board')
            user.profile.grade = form.cleaned_data.get('grade')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'register.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')


