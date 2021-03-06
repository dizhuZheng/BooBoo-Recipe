from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponse
from .forms import ProfileForm
from recipes.models import Post
from .es_call import esearch
import json


def profile(request, username):
    '''show my profile'''
    p = UserProfile.objects.get(username=username)
    return render(request, 'users/profile.html', {'user':request.user, 'p': p})


def my_posts(request, username):
    all_posts = UserProfile.objects.prefetch_related('post_author').get(username=username)
    my_posts = all_posts.post_author.filter(status=1)
    return render(request, 'users/my_posts.html', {'my_posts': my_posts})


@login_required
def my_drafts(request):
    all_drafts = UserProfile.objects.prefetch_related('post_author').get(username=request.user.username)
    my_drafts = all_drafts.post_author.filter(status=0)
    return render(request, 'users/my_drafts.html', {'user':request.user, 'my_drafts': my_drafts})


@csrf_protect
@login_required
def change_profile(request, username):
    '''更新个人资料'''
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Personal Information has been updated！')
            return redirect("users:profile", username=request.user.username)
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/change_profile.html', context={'form': form, 'username': username})


def my_saves(request, username):
    user = UserProfile.objects.get(username=username)
    my_saves = user.post_favo.all()
    return render(request, 'users/my_saves.html', {'user':user, 'my_saves': my_saves})


def search_index(request):
    results = []
    query = request.GET.get('q')
    results = esearch(username=query, gender=query, email=query, address=query)
    context = {'results': results, 'count': len(results), 'search_term': query}
    return render(request, 'users/index.html', context)
