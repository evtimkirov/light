from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from rest_framework import generics
from .models import Terminal
from .serializers import TerminalSerializer, TerminalDetailsSerializer

## Terminal page methods
# Terminals listing
def index(request):
    template = loader.get_template('terminals/list.html')
    terminals = Terminal.objects.all().filter(in_stock=True).order_by('-id')
    paginator = Paginator(terminals, 1)

    context = {'terminals' : paginator.get_page(request.GET.get('page'))}

    return HttpResponse(template.render(context, request))

# Terminal details
def detail(request, terminal_id):
    template = loader.get_template('terminals/detail.html')
    terminal = Terminal.objects.get(id=terminal_id)
    context = {
        'terminal' : terminal,
    }

    return HttpResponse(template.render(context, request))

## Terminal API methods
# Terminals API
class TerminalsAPIView(generics.ListAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

# Terminal details API
class TerminalDetailsAPIView(generics.RetrieveAPIView):
    queryset = Terminal.objects.all()
    serializer_class = TerminalDetailsSerializer