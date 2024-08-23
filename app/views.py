from django.shortcuts import render
from datetime import date

from.models import Tarefa

def index(request):
    hoje = date.today

    terefas = Tarefa.objects.all()

    context = {
        'tarefas': terefas,
        'hoje': hoje,
    }

    return render(request, 'index.html', context)