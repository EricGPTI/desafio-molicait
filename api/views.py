from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transacao

# Create your views here.

@api_view(['POST'])
def troco(request):
    if request.method == 'POST':
        total = request.POST.get['total']
        pago = request.POST.get['pago']
        transacao = Transacao()
        session = request.POST.get['session']
        print(session)
