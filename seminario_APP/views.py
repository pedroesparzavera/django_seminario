from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm


# Vista del index
def home(request):
    return render(request, 'index.html', {
        'links': {
            'inscrito_list': 'Listar Participantes',
            'inscrito_create': 'Agregar Participante',
        }
    })


# Seccion Inscritos
class InscritoListView(generic.ListView):
    model = Inscrito
    template_name = 'inscrito_list.html'
    context_object_name = 'inscritos'
    paginate_by = 15  # Muestra 15 registros por página

    def get_queryset(self):
        # Obtener el parámetro de ordenamiento desde la URL
        order_by = self.request.GET.get('order_by', 'recent')  # Predeterminado: Más Recientes
        if order_by == 'id':
            return Inscrito.objects.all().order_by('id')  # Ordenar por ID ascendente
        return Inscrito.objects.all().order_by('-fecha_inscripcion', '-hora_inscripcion')  # Más Recientes


class InscritoCreateView(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'

    def form_valid(self, form):
        # Guardar el registro en la base de datos
        form.save()
        messages.success(self.request, "¡Registro exitoso! El participante fue inscrito correctamente.")
        # Renderizar la misma página con un formulario limpio
        return self.render_to_response(self.get_context_data(form=self.form_class(), institucion_form=InstitucionForm()))

    def form_invalid(self, form):
        # Mostrar mensaje de error si el formulario no es válido
        messages.error(self.request, "Hubo un error al registrar el participante. Por favor, revise los campos.")
        return self.render_to_response(self.get_context_data(form=form, institucion_form=InstitucionForm()))

    def get_context_data(self, **kwargs):
        # Añadir el formulario de creación de instituciones
        context = super().get_context_data(**kwargs)
        context['institucion_form'] = kwargs.get('institucion_form', InstitucionForm())
        return context

    def get_success_url(self):
        # Retorna None para evitar redirección
        return None

class InscritoUpdateView(generic.UpdateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'
    success_url = reverse_lazy('inscrito_list')


class InscritoDeleteView(generic.DeleteView):
    model = Inscrito
    template_name = 'inscrito_confirm_delete.html'
    success_url = reverse_lazy('inscrito_list')


# Seccion de institucion 
class InstitucionCreateView(CreateView):
    model = Institucion
    fields = ['nombre']
    template_name = 'institucion_form.html'
    success_url = reverse_lazy('inscrito_create')  # Redirige al formulario de inscripción

    def form_valid(self, form):
        messages.success(self.request, "¡Institución creada exitosamente!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al crear la institución. Intente nuevamente.")
        return super().form_invalid(form)




# Vistas basadas en funciones para Instituciones
def institucion_list(request):
    instituciones = Institucion.objects.all()  # Obtener todas las instituciones
    return render(request, 'institucion_list.html', {'instituciones': instituciones})


def institucion_detail(request, id):
    institucion = get_object_or_404(Institucion, id=id)
    return JsonResponse({'id': institucion.id, 'nombre': institucion.nombre})


def bulk_delete_inscritos(request):
    if request.method == 'POST':
        seleccionados = request.POST.getlist('seleccionados')
        if seleccionados:
            Inscrito.objects.filter(id__in=seleccionados).delete()
            messages.success(request, "Los registros seleccionados han sido eliminados exitosamente.")
        else:
            messages.error(request, "No seleccionaste ningún registro para eliminar.")
    return HttpResponseRedirect(reverse('inscrito_list'))

# Vista para actualizar una institución
class InstitucionUpdateView(UpdateView):
    model = Institucion
    fields = ['nombre']
    template_name = 'institucion_form.html'
    success_url = reverse_lazy('institucion_list')

    def form_valid(self, form):
        messages.success(self.request, "¡Institución actualizada exitosamente!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar la institución. Intente nuevamente.")
        return super().form_invalid(form)

# Vista para eliminar una institución
class InstitucionDeleteView(DeleteView):
    model = Institucion
    template_name = 'institucion_confirm_delete.html'
    success_url = reverse_lazy('institucion_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "¡Institución eliminada exitosamente!")
        return super().delete(request, *args, **kwargs)