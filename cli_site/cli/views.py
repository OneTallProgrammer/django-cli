from django.shortcuts import render
from cli.models import * 

def cli(request):
    commands = Command.objects.all().order_by('cmd')
    return render(request, 'cli/index.html', {'commands' : commands})
