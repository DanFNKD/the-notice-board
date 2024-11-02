from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Vote, UserProfile
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, UserProfileForm
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    post_list = Post.objects.filter(status=1)
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'post_list': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, "blog/index.html", context)

# Detail view for a post 
def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

# creating a post
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.save()
            messages.success(request, "Your post is live!")
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})

# voting for upvoting and downvoting
@login_required
def vote(request, post_id, vote_value):
    post = get_object_or_404(Post, id=post_id)
    vote_value = int(vote_value)

    vote, created = Vote.objects.update_or_create(
        user=request.user, post=post,
        defaults={'value': vote_value}
    )

    if created:
        messages.success(request, "Thank you for your feedback!")
    else:
        messages.info(request, "You have already voted on this post.")

    return redirect('post_detail', slug=post.slug)

# User profile view
def profile_view(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    user_posts = Post.objects.filter(author=user_profile.user, status=1).order_by('-created_on')
    return render(request, 'blog/profile.html', {
        'user_profile': user_profile,
        'user_posts': user_posts
    })

# Edit profile view
def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect("profile", username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, "blog/edit_profile.html", {"form": form})
