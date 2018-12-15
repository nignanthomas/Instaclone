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
@login_required(login_url='/accounts/login/')
def timeline(request):
    current_user=request.user
    posts= Post.objects.all()
    profiles= Profile.objects.all()
    # form=CommentForm()
    # comments=Comment.objects.all()
    return render(request,'timeline.html',{"posts":posts,"profiles":profiles})
