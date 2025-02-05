from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author':'John Igoche',
        'title':'Hello World Post',
        'content':'I am happy to make my first ever post on here, cheers!',
        'date_posted':'5th February 2025.'
    },
    {   'author': 'Daniel Ekpo',
        'title': 'My First Post',
        'content': 'Wow, I am happy to also make my first ever post on here, cheers!',
        'date_posted': '4th February 2025.'}
]

def home(request):
    context = {
        'data':posts
    }
    return render(request, "blog/home.html", context=context)


def about(request):
    return render(request, "blog/about.html", {'title':'About'})
