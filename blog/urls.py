from .import views
from django.urls import path
import django_summernote

urlpatterns = [
    path('', views.post_list, name='home'),
    path('create-post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('post/<int:post_id>/vote/<slug:vote_value>/', views.vote, name='vote'),
]