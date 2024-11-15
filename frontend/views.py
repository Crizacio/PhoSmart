from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "frontend/index.html", {
        "temperatura": "24°C",
        "humedad": "17%",
        "lux": "329",
        "actuadores": {
            "cortina": "60%",
            "luz": "30%"
        }
    })
