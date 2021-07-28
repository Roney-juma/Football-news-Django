from django.shortcuts import render
 

# Create your views here.

def home(request):
    import requests
    import json
    api_request = requests.get("https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=384e999ffb31459da519c72d9c8f6ba2")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api' : api})
