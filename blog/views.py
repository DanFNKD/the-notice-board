from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Vote
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

# Detail view for a post 
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

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
            if not post.slug:
                post.slug = slugify(post.title)
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