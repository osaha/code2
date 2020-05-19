from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BookRequest, BookData
import requests

# Create your views here.
def top(request):
    return render(request, 'feedbook/top.html',{})

class BookRequestListView(ListView):
    model = BookRequest


class BookRequestDetailView(DetailView):
    model = BookRequest
    context_object_name = 'book_request'


class BookRequestCreateViwq(CreateView):
    model = BookRequest
    # undifined


class BookDataCreateView(CreateView):
    model = BookData
    fields = ('isbn', 'title', 'author', 'published_company','published_year' ,)
    template_name = 'feedbook/bookdata_form.html'
    success_url = '/'


