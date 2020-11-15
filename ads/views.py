from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ad
# Create your views here.
class AdListView(ListView):
    pass


class AdDetailView(DetailView):
    pass


class AdCreateView(CreateView):
    pass


class AdUpdateView(UpdateView):
    pass


class AdDeleteView(DeleteView):
    pass