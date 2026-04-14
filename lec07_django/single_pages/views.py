from django.shortcuts import render

# Create your views here.

def about_page(request):
    return render(request, "single_pages/about_me.html")

def landing_page(request):
    return render(request, "single_pages/landing.html")

def blog_list(request):
    return render(request, "single_pages/blog_list.html")