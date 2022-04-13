from django.shortcuts import render

from AppSeller.forms import FormularioSeller
from AppSeller.models import Producto

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def publicar(request):

    if request.method == "POST":
        formSeller = FormularioSeller(request.POST)

        if formSeller.is_valid():

            info = formSeller.cleaned_data
            producto = Producto(user_id = '1', titulo = info['titulo'], descripcion = info['descripcion'], precio = info['precio'], fecha_publicacion = info['fecha_publicacion'])

            producto.save()

            return render(request, "inicio.html")

    else: 

        formSeller = FormularioSeller()

    return render(request, 'productoFormulario.html', {'formSeller': formSeller})
            