from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile,Comment
from .forms import NewPostForm,ProfileForm,CommentForm
# from .forms import PostForm,LocationForm,ProfileForm,CommentForm
# from django.http import JsonResponse
# import json
from django.db.models import Q

# Create your views here.
@login_required(login_url='/accounts/login/')
def timeline(request):
    posts= Post.objects.all()
    profiles= Profile.objects.all()
    current_user = request.user

    comments=Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = int(request.POST.get("idpost"))
            post = Post.objects.get(id = post_id)
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = post
            comment.save()
        return redirect('timeline')

    else:
        form = CommentForm()

    return render(request,'timeline.html',{"posts":posts,"profiles":profiles,"current_user":current_user,"comments":comments,"form":form,})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_users = Profile.search_profile(search_term)
        message=f"Search results for: {search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term."
        return render(request,'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def explore(request):
    posts = Post.objects.all()
    profiles= Profile.objects.all()[:3]
    # form=CommentForm()
    # comments=Comment.objects.all()
    return render(request,"explore.html",{"posts":posts,"profiles":profiles,})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    user_object = request.user
    current_user = Profile.objects.get(username__id=request.user.id)
    user = Profile.objects.get(username__id=id)
    posts = Post.objects.filter(upload_by = user)
    return render(request, "profile.html", {"current_user":current_user,"posts":posts,"user":user,"user_object":user_object,})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = Profile.objects.get(username__id=request.user.id)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.upload_by = current_user
            post.save()
        return redirect('timeline')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


# def comment():
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.username = request.user
#             comment.post = post
#             comment.save()
#         return redirect('timeline')
#
#     else:
#         form = CommentForm()

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
            # new_name = form.cleaned_data["fullname"]
            # new_bio = form.cleaned_data["bio"]
            # new_email = form.cleaned_data["email"]
            # new_phonenumber = form.cleaned_data["phonenumber"]
            # new_gender = form.cleaned_data["gender"]
            # new_pic = form.cleaned_data["profile_pic"]
            # profile=form.save(commit=False)
            # profile.username = current_user
            # profile.save()
            # user_edit.update(fullname = new_name,bio = new_bio,email = new_email,phonenumber = new_phonenumber,gender = new_gender,profile_pic = new_pic)
    else:
        form=ProfileForm(instance=request.user.profile)
        print('error')


    return render(request,'edit_profile.html',locals())
