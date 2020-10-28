from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Auto, Make
from .forms import MakeForm, AutoForm
# Create your views here.


class MainView(LoginRequiredMixin, View):

    template = 'autos/auto_list.html'

    def get(self, request):

        auto_list = Auto.objects.all()
        make_count = Make.objects.all().count()
        ctx = {'auto_list': auto_list, 'make_count': make_count}
        
        return render(request, self.template, ctx)


class AutoCreate(LoginRequiredMixin, CreateView):

    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):

    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):

    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Inside the CreateView, UpdateView and DeleteView 

# class AutoCreate(View):

#     template = 'autos/auto_form.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request):
#         form = AutoForm()
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = AutoForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(reqeust, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)



# class AutoUpdate(View):
    
#     model = Auto
#     template = 'autos/auto_form.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request, pk):
#         auto = get_object_or_404(self.model, pk=pk)
#         form = AutoForm(instance=auto)
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         auto = get_object_or_404(self.model, pk=pk)
#         form = AutoForm(request.POST, instance=auto)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)



# class AutoDelete(View):

#     model = Auto
#     template = 'autos/auto_confirm_delete.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request, pk):
#         auto = get_object_or_404(self.model, pk=pk)
#         ctx = {'auto': auto}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         auto = get_object_or_404(self.model, pk=pk)
#         auto.delete()
#         return redirect(self.success_url)




# class MakeView(View):

#     template = 'autos/make_list.html'

#     def get(self, request):

#         make_list = Make.objects.all()
#         ctx = {'make_list': make_list}
#         return render(request, self.template, ctx)
class MakeView(LoginRequiredMixin, ListView):
    
    model = Make
    template = 'autos/make_list.html'


class MakeCreate(LoginRequiredMixin, CreateView):

    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, UpdateView):

    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):

    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
# class MakeCreate(View):

#     template = 'autos/make_form.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request):

#         form = MakeForm()
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request):

#         form = MakeForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         form.save()
#         return redirect(self.success_url)
            


# class MakeUpdate(View):

#     model = Make
#     template = 'autos/make_form.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(instance=make)
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(request.POST, instance=make)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)




# class MakeDelete(View):

#     model = Make
#     template = 'autos/make_confirm_delete.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         ctx = {'make': make}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
#         return redirect(self.success_url)





























