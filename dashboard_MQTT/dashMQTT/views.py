from django.shortcuts import render
from .mqtt_client import latest_message

def dashboard(request):
    context = {
        'mqtt_data': latest_message
    }
    return render(request, 'dashMQTT/dashboard.html', context)