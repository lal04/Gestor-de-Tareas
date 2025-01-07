from django.urls import reverse_lazy
from .models import Tarea
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)

class TareaCreateView(CreateView):
    model=Tarea
    fields=['nombre', 'descripcion']
    template_name='tarea_form.html'
    success_url=reverse_lazy('tarea_list')
    
class TareaListView(ListView):
    model=Tarea
    template_name='tarea_list.html'
    
    
class TareaUpdateView(UpdateView):
    model=Tarea
    fields='__all__'
    template_name='tarea_form.html'
    success_url=reverse_lazy('tarea_list')

class TareaDeleteView(DeleteView):
    model=Tarea
    success_url=reverse_lazy('tarea_list')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    
class TareaDetailView(DetailView):
    model=Tarea
    template_name='tarea_detail.html'
    
    
