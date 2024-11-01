import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from blog.models import Post

# Check for posts without slugs
posts_without_slug = Post.objects.filter(slug__isnull=True) | Post.objects.filter(slug='')

if posts_without_slug.exists():
    print("Posts without a slug:")
    for post in posts_without_slug:
        print(f"Post ID: {post.id}, Title: '{post.title}', Slug: '{post.slug}'")
else:
    print("No posts without a slug found.")