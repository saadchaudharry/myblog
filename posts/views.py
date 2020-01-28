from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost
# Create your views here.


class home(ListView):
    model = BlogPost
    paginate_by = 3
    template_name = 'home.html'



class detail(DetailView):
    model = BlogPost
    template_name = "detail.html"

