from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import File, Display
from django.forms import Textarea
from django import forms
from .decorators import basicauth
from django.utils.decorators import method_decorator


class DisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = (
            'name',
            'ip_address',
            'username',
            'ssh_public_key_or_password',
            'remote_directory',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'ssh_public_key_or_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'remote_directory': forms.TextInput(attrs={'class': 'form-control'}),
        }

@method_decorator(basicauth, name='dispatch')
class DisplayListView(ListView):
    model = Display
    template_name = 'display/display_list.html'
    context_object_name = 'displays'

@method_decorator(basicauth, name='dispatch')
class DisplayCreateView(CreateView):
    model = Display
    template_name = 'display/display_form.html'
    success_url = reverse_lazy('display-list')
    form_class = DisplayForm

@method_decorator(basicauth, name='dispatch')
class DisplayUpdateView(UpdateView):
    model = Display
    template_name = 'display/display_form.html'
    success_url = reverse_lazy('display-list')
    form_class = DisplayForm

@method_decorator(basicauth, name='dispatch')
class DisplayDeleteView(DeleteView):
    model = Display
    template_name = 'display/display_confirm_delete.html'
    success_url = reverse_lazy('display-list')

@method_decorator(basicauth, name='dispatch')
class FileListView(ListView):
    model = File
    template_name = 'file/file_list.html'
    context_object_name = 'files'

@basicauth
def manage_file_assignments(request, file_id):
    file = File.objects.get(pk=file_id)
    if request.method == 'POST':
        display_ids = request.POST.getlist('displays')
        displays = Display.objects.filter(pk__in=display_ids)
        file.displays.set(displays)
        return redirect('file-list')
    else:
        displays = Display.objects.all()
        assigned_displays = file.displays.all()
        return render(request, 'file/manage_file_assignments.html', {'file': file, 'displays': displays, 'assigned_displays': assigned_displays})

@method_decorator(basicauth, name='dispatch')
class FileCreateView(CreateView):
    model = File
    fields = ['name', 'file']
    template_name = 'file/file_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('file-list')

@method_decorator(basicauth, name='dispatch')
class FileDeleteView(DeleteView):
    model = File
    template_name = 'file/file_confirm_delete.html'  # You can create this template for confirmation
    success_url = reverse_lazy('file-list')  # Redirect to the file list after deletion