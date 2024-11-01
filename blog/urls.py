from .import views
from django.urls import path
import django_summernote

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('create-post/', views.create_post, name='create_post'),
    path("post/<int:post_id>/vote/<slug:vote_value>/", views.vote, name="vote"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]