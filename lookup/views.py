from django.shortcuts import render
import json
import requests


# Create your views here.
def home(request):

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        if zipcode == "" : zipcode = "20002"
    else:
        zipcode="20002"
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=E8BFDE01-FE71-40F2-87A2-3BFEA75230E8")
    api = json.loads(api_request.content)
    try:
        CatName = api[0]['Category']['Name']
        if CatName == "Good":
            catcolor = "good"
            fontcolor = "black"
        if CatName == "Moderate":
            catcolor = "moderate"
            fontcolor = "black"
        if CatName == "USG":
            catcolor = "usg"
            fontcolor = "white"
        if CatName == "Unhealthy":
            catcolor = "unhealthy"
            fontcolor = "white"
        if CatName == "VeryUnhealthy":
            catcolor = "veryunhealthy"
            fontcolor = "white"
        if CatName == "Hazardous":
            catcolor = "hazardous"
            fontcolor = "white"

        return render(request, 'home.html',{'api':api, 'category_color':catcolor,'fontcolor':fontcolor})
    except Exception:
        api = "Error!!!"
        return render(request,'home.html',{'api':api})

def about(request):
    return render(request, 'about.html')
