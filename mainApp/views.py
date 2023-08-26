from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, City, Country
# Create your views here.
def index_view(request):
    allData = Book.objects.all()
    infoData = []
    for data in allData:
        placejson = {}
        placejson ['id'] = data.id
        placejson ['title'] = data.title
        placejson ['authorName'] = data.author.name
        infoData.append(placejson)
    print("data",infoData )
    return render(request, 'mainApp/index.html', {"bookInfo":infoData})
def deleteData(request):
    data = Author.objects.filter(id =6).delete()
    if not data:
        return HttpResponse('Data Deleted')
    else:
        return HttpResponse('Data Not Deleted')
    
def CityInfo(request):
    allData = City.objects.all()
    infoData = []
    for data in allData:
        placejson = {}
        placejson['id'] = data.id
        placejson['cityName'] = data.name
        placejson['population'] = data.population
        placejson['continent'] = data.continent
        placejson['countryName'] = data.country.name
        placejson['independent'] = data.country.becameIndependent
        infoData.append(placejson)
    print("data",infoData )
    return render(request, 'mainApp/city.html', {"cityInfo":infoData})

def DeleteCity(request):
    data = Country.objects.filter(id = 1).delete()
    if data:
        return HttpResponse("Deleted Country")
    else:
        return HttpResponse("Not Deleted Country")

    
