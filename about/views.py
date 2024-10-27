from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    about = About.objects.order_by('-updated_on').first()

    if not about:
        about = None

    return render(
        request,
        "about/about.html",
        {"about": about},
    )