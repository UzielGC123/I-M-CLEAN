from django.shortcuts import render , get_object_or_404, redirect
from django.db.models import Q
from .models import Cliente

#autores uziel y brenda

def registrar_cliente (request):
    
    if request.method == 'POST':

        v_usuario = request.POST['usuario']
        v_apellido = request.POST['apellido']
        v_correo = request.POST['correo']
        v_password = request.POST['password']
        v_telefono = request.POST['telefono']
        v_adiccion = request.POST['adiccion']

        cliente_nuevo = Cliente(
            usuario=v_usuario,
            apellido=v_apellido,
            correo=v_correo,
            password=v_password,
            telefono=v_telefono,
            adiccion=v_adiccion
        )

        cliente_nuevo.save()

        return render (request, 'registroCliente.html',{
            'mensaje': "Cliente registrado con exitoen la DB"
        })
    return render(request,'registroCliente.html')

def buscar_users (request):
    resultados = []
    query = request.GET.get('consultar_usuario')

    if query:
        resultados = Cliente.objects.filter(
            Q(usuario__icontains=query) | Q(telefono__icontains=query)
        )
    return render(request, 'buscar.html', {'resultados':resultados})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        cliente.usuario = request.POST.get('usuario', cliente.usuario)
        cliente.apellido = request.POST.get('apellido', cliente.apellido)
        cliente.correo = request.POST.get('correo', cliente.correo)
        cliente.password = request.POST.get('password', cliente.password)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.adiccion = request.POST.get('adiccion', cliente.adiccion)
        cliente.save()
        return redirect('buscar_usuarios')
    
    return render(request, 'editar_cliente.html', {'cliente': cliente})

def eliminar_cliente (request, cliente_id):
    cliente_a_borrar= get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        cliente_a_borrar.delete()
        return redirect('buscar_usuarios')
    return render (request, 'eliminar_cliente.html', {'cliente': cliente_a_borrar})

def index(request):
    return render(request, 'index.html')


