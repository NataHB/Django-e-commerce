from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from mi_app.models import Producto, Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#VISTAS SIN LOGIN
class HomeView(TemplateView):
    template_name = 'mi_app/index.html'

class AboutView(TemplateView):
    template_name = 'mi_app/about.html'


# PASTELERIA
class PasteleriaView( ListView):
    model = Producto
    context_object_name = 'pasteleria'
    template_name = 'mi_app/pasteleria_list.html'

class PasteleriaDetailView( DetailView):
    model = Producto
    context_object_name = 'pasteleria'
    template_name = 'mi_app/pasteleria_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()  # Filtra comentarios por producto
        return context


# BEBIDAS
class BebidaView( ListView):
    model = Producto
    context_object_name = 'bebidas'
    template_name = 'mi_app/bebidas_list.html'

class BebidaDetailView( DetailView):
    model = Producto
    context_object_name = 'bebidas'
    template_name = 'mi_app/bebidas_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()  # Filtra comentarios por producto
        return context


# COMENTARIOS
class ComentariosCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = [ 'producto', 'mensaje']
    template_name = 'mi_app/comentario.html'

    def form_valid(self, form):
        form.instance.pasteleria_id = self.kwargs['pk']  # Vincula el comentario con la pasteleria/producto
        form.instance.nombre = self.request.user
        return super().form_valid(form)

    def get_success_url(self):       
        return reverse_lazy('pasteleria_detail', kwargs={'pk': self.object.pasteleria_id})
    
class ComentariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'mi_app/comentario_confirm_delete.html'
    success_url = reverse_lazy('index')

class ComentariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = [ 'producto', 'mensaje']
    template_name = 'mi_app/comentario_update.html'
    success_url = reverse_lazy('index')
