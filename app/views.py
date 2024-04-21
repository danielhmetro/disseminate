from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Display

class DisplayListView(ListView):
    model = Display
    template_name = 'display/display_list.html'
    context_object_name = 'displays'

class DisplayCreateView(CreateView):
    model = Display
    template_name = 'display/display_form.html'
    fields = ['name', 'ip_address', 'username', 'ssh_public_key_or_password', 'remote_directory']
    success_url = reverse_lazy('display-list')

class DisplayUpdateView(UpdateView):
    model = Display
    template_name = 'display/display_form.html'
    fields = ['name', 'ip_address', 'username', 'ssh_public_key_or_password', 'remote_directory']
    success_url = reverse_lazy('display-list')

class DisplayDeleteView(DeleteView):
    model = Display
    template_name = 'display/display_confirm_delete.html'
    success_url = reverse_lazy('display-list')
