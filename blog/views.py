from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Vote, UserProfile, Tag
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, UserProfileForm
from django.core.paginator import Paginator
from django.db.models import Count
from django.utils.text import slugify
import time

def post_list(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort')
    selected_tag = request.GET.get('tag')

    # Initial post query for published posts
    post_list = Post.objects.filter(status=1).order_by('-created_on')

    # Apply search filtering
    if query:
        post_list = post_list.filter(title__icontains=query)
    
    # Apply tag filtering if selected
    if selected_tag:
        post_list = post_list.filter(tags__name=selected_tag)

    # Annotate with vote count for sorting by popularity
    post_list = post_list.annotate(vote_count=Count('votes'))

    # Apply sorting based on query
    if sort == 'date':
        post_list = post_list.order_by('-created_on')
    elif sort == 'title':
        post_list = post_list.order_by('title')
    elif sort == 'popularity':
        post_list = post_list.order_by('-vote_count')

    # Pagination: Show 6 posts per page
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch all tags for filtering dropdown
    tags = Tag.objects.all()

    # Context with page_obj as post_list
    context = {
        'post_list': page_obj,  # paginated posts
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'query': query,
        'sort': sort,
        'selected_tag': selected_tag,
        'tags': tags,
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

            post.slug = slugify(post.title) if post.title else 'default-slug'
            
            # Determine post status based on user role
            if request.user.is_staff:
                post.status = 1  # Published status
                messages.success(request, "Your post has been published successfully!")
            else:
                post.status = 0  # Draft status (for pending approval)
                messages.success(request, "Your post has been submitted for approval and will be live once approved!")
            
            # Save the post
            post.save()
            form.save_m2m() 
            
            return redirect("profile", username=request.user.username)
    
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
@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    user_posts = Post.objects.filter(author=user_profile.user, status=1).order_by('-created_on')
    return render(request, 'blog/profile.html', {
        'user_profile': user_profile,
        'user_posts': user_posts
    })

# Edit profile view
@login_required
def edit_profile(request):
    # Get or create the user's profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully.")
            return redirect("profile", username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "blog/edit_profile.html", {"form": form})
