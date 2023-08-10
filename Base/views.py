from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Post, Comentario
from .forms import ActualizacionPost, FormularioCambioPassword, FormularioEdicion, FormularioNuevoPost, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})

# TECLADO

class TecladoDetalle(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'teclado'
    template_name = 'tecladoDetalle.html'

class TecladoUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = ActualizacionPost
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'tecladoEdicion.html'

class TecladoDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'tecladoBorrado.html'

# CREACION Post

class PostCreacion(LoginRequiredMixin, CreateView):
    model = Post
    form_class = FormularioNuevoPost
    success_url = reverse_lazy('home')
    template_name = 'postCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)