from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, CreateView
from django.db.models import Q

from blog.views import BaseView
from .forms import ProfileUpdateForm, SignUpForm

from accounts.models import CustomUser


class SignUpPage(CreateView, BaseView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login_page')

    def get_context_data(self, **kwargs):
        context = super(SignUpPage, self).get_context_data()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context

class LoginPage(View, BaseView):
    def get(self, request):
        context = {
            'categories':self.category(),
            'tags':self.tag()
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password error!')
            return redirect('login_page')

def logout_page(request):
    logout(request)
    return redirect('login_page')

class UserProfile(View, BaseView):
    def get(self, request):
        username = request.user.username
        profile = CustomUser.objects.get(username=username)
        context = {
            'profile':profile,
            'categories':self.category(),
            'tags':self.tag()
        }

        return render(request, 'accounts/profile.html', context)


class UserUpdate(UpdateView, BaseView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context

class UserList(View):
    def get(self, request):
        search = request.GET.get('search')


        if search:
            users = CustomUser.objects.filter(
                Q(username__icontains=search) | Q(email__icontains=search)
            )
        else:
            users = CustomUser.objects.all()

        context = {
            'users':users
        }
        return render(request, 'accounts/users.html', context)