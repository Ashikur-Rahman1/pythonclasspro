from django.shortcuts import render
from django.views import generic
from .models import post

# Create your views here.

class postlist(generic.ListView):
    queryset = post.objects.filter(status=1).ordering_by('-created_on')
    template_name = 'index.html'
    class postdetails(generic.DetailView):
        model = post
        template_name = 'postdetails.html'
