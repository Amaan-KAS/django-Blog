from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

posts = [

    {
        'author': 'CoreyMS',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted':'August 27, 2021'
    },
    {
        'author': 'JoreyMS',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted':'August 28, 2021'
    },
        {
        'author': 'MS',
        'title' : 'Blog Post 3',
        'content': 'Third post content',
        'date_posted':'August 29, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

