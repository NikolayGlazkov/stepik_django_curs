from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, InnForm
from .models import Client
from django.http import HttpResponse


# Представление для стартовой страницы
def index(request):
    return render(request, 'ferst/index.html')

# добавить запись в базу данных
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_clients')
    else:
        form = ClientForm()

    return render(request, 'ferst/client_form.html', {'form': form})

def show_clients(request):
    clients = Client.objects.all()
    return render(request, 'ferst/show_clients.html', {'clients': clients})

def index(request):
    inn_form = InnForm()
    return render(request, 'ferst/index.html', {'inn_form': inn_form})


def edit_client(request, inn=None):
    client = get_object_or_404(Client, inn=inn) if inn else None

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('show_clients')
    else:
        form = ClientForm(instance=client)

    return render(request, 'ferst/edit_client.html', {'form': form, 'client': client})