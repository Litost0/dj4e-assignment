from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat, Breed



class MainView(LoginRequiredMixin, View):

    template = 'cats/cat_list.html'

    def get(self, request):

        cat_list = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        ctx = {'cat_list': cat_list, 'breed_count': breed_count}
        
        return render(request, self.template, ctx)


class CatCreate(LoginRequiredMixin, CreateView):

    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):

    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):

    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedView(LoginRequiredMixin, ListView):
    
    model = Breed
    template = 'cats/breed_list.html'


class BreedCreate(LoginRequiredMixin, CreateView):

    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):

    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):

    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

