from django.shortcuts import render
from .models import Servicio
from django.views.generic import DetailView

# Create your views here.


def servicios(request):
    return render(request, 'servicios/servicios.html')


class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'servicios/servicio_detail.html'
    context_object_name = 'servicio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios'] = Servicio.objects.all()
        return context
