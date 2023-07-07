from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login

# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def contactos(request):
    return render(request, 'core/contactos.html')

def eventos(request):
    return render(request, 'core/eventos.html')



def register(request):
    data = {
        'form': RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect(to='login')
        data ["form"] = formulario
    return render(request, 'registration/registro.html',data)


def info(request):
    return render(request, 'core/info.html')

@login_required
def tienda1(request):
    data = {
            'form': PedidoTiendaForm(request.POST)
        }
    if request.method == 'POST':
        username = request.POST['username']
        formulario = PedidoForm(request.POST,cliente=username)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
        else:
            data['mensaje'] = "try again :("
    return render(request, 'core/tienda.html', data)

@login_required
def tienda(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PedidoTiendaForm(request.POST, user=request.user)
            print(form.errors)
            if form.is_valid():
                # Realizar alguna acción con el formulario y el usuario cliente
                
                # Por ejemplo, guardar el formulario si es necesario
                
                form.save()
                
                
                # O realizar alguna otra acción que necesites
        else:
            form = PedidoTiendaForm(user=request.user)
        
        return render(request, 'core/tienda.html', {'form': form})
    else:
        # El usuario no está autenticado, realiza alguna acción o redirige a otro lugar
        pass



def login(request):
    return render(request, 'registration/login.html')

@permission_required('app.add_concierto')
def Gestion(request):

    concierto = Concierto.objects.all()
    Pag_Concierto = Paginator(concierto,5)
    pag_number_C = request.GET.get('page_c')
    concierto = Pag_Concierto.get_page(pag_number_C)

    entrada = Entrada.objects.all()
    Pag_Entrada = Paginator(entrada,5)
    pag_number_E = request.GET.get('page_e')
    entrada = Pag_Entrada.get_page(pag_number_E)

    cliente = User.objects.all()
    Pag_cliente = Paginator(cliente,5)
    pag_number_Cli = request.GET.get('page_cli')
    cliente = Pag_cliente.get_page(pag_number_Cli)

    pedido = Pedido.objects.all()
    Pag_pedido = Paginator(pedido,5)
    pag_number_p = request.GET.get('page_p')
    pedido = Pag_pedido.get_page(pag_number_p)

    data = {
            'Concierto':concierto,
            'Entrada':entrada,
            'Cliente':cliente,
            'Pedido':pedido
    }
    return render(request, 'core/Gestion.html',data)

@permission_required('app.add_concierto')
def CrearConcierto(request):
    data = {
        'form':ConciertoForm()
    }
    if request.method == 'POST':
        formulario = ConciertoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
    return render(request,'core/Crear.html',data)

@permission_required('app.add_concierto')
def CrearEntrada(request):
    data = {
        'form':EntradaForm()
    }
    if request.method == 'POST':
        formulario = EntradaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
    return render(request,'core/Crear.html',data)

@permission_required('app.add_concierto')
def CrearCliente(request):
    data = {
        'form':ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
    return render(request,'core/Crear.html',data)

@permission_required('app.add_concierto')
def CrearPedido(request):
    data = {
        'form':PedidoForm()
    }
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
    return render(request,'core/Crear.html',data)


@permission_required('app.add_concierto')
def ModificarConcierto(request,id):
    concierto = Concierto.objects.get(id=id)
    data = {
        'form':ConciertoForm(instance=concierto)
    }
    if request.method == 'POST':
        formulario = ConciertoForm(data=request.POST, instance=concierto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request,'core/Modificar.html',data)

@permission_required('app.add_concierto')
def ModificarEntrada(request,id):
    entrada = Entrada.objects.get(id=id)
    data = {
        'form':EntradaForm(instance=entrada)
    }
    if request.method == 'POST':
        formulario = EntradaForm(data=request.POST, instance=entrada)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request,'core/Modificar.html',data)

@permission_required('app.add_concierto')
def ModificarCliente(request,username):
    cliente = User.objects.get(username=username)
    data = {
        'form':ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request,'core/Modificar.html',data)


@permission_required('app.add_concierto')
def ModificarPedido(request,id):
    pedido = Pedido.objects.get(id=id)
    data = {
        'form':PedidoForm(instance=pedido)
    }
    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request,'core/Modificar.html',data)




@permission_required('app.add_concierto')
def EliminarConcierto(request,id):
    concierto = Concierto.objects.get(id=id)
    concierto.delete()
    
    return redirect(to='Gestion')

@permission_required('app.add_concierto')
def EliminarEntrada(request,id):
    entrada = Entrada.objects.get(id=id)
    entrada.delete()
    
    return redirect(to='Gestion')

@permission_required('app.add_concierto')
def EliminarCliente(request,username):
    cliente = User.objects.get(username=username)
    cliente.delete()
    
    return redirect(to='Gestion')

@permission_required('app.add_concierto')
def EliminarPedido(request,id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    
    return redirect(to='Gestion')