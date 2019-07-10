from django.shortcuts import render
from cli.models import * 
from cli.forms import *

def cli(request):
    agent_interface = CLI()
    
    if request.POST:
        print("We are here")
        print(request)
        print("We are exiting")

    commands = Command.objects.all().order_by('cmd')
    return render(request, 'cli/index.html', {'agent_interface' : agent_interface})
