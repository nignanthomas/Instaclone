from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile
# from .forms import PostForm,LocationForm,ProfileForm,CommentForm
# from django.http import JsonResponse
# import json
from django.db.models import Q

# Create your views here.
# @login_required(login_url='/accounts/login/')
def timeline(request):
    posts= Post.objects.all()
    profiles= Profile.objects.all()
    # form=CommentForm()
    # comments=Comment.objects.all()
    return render(request,'timeline.html',{"posts":posts,"profiles":profiles})


# @login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_users = Profile.search_profile(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term."
        return render(request,'search.html',{"message":message})


# @login_required(login_url='/accounts/login/')
def explore(request):
    posts = Post.objects.all()
    # form=CommentForm()
    # comments=Comment.objects.all()
    return render(request,"explore.html",{"posts":posts,})
