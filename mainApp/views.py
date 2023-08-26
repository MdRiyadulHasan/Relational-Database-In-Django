from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, City, Country, CourseInfo, Student
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

def CourseView(request):
    allData =   CourseInfo.objects.all()
    infoData = []
    for data in allData:
        placejson = {}
        placejson['id'] = data.id
        placejson['title'] = data.title

        student_list =  []
        for student in data.students.all():
            student_list.append(student.name)
        placejson['students'] = student_list

        infoData.append(placejson)
    print("Information", infoData)
    return render(request, 'mainApp/course.html')

def course_list(request):
    all_data = CourseInfo.objects.all()
    info_data = []
    for data in all_data:
        place_json = {
            'id': data.id,
            'title': data.title,
            'students': [student.name for student in data.students.all()]
        }
        info_data.append(place_json)
    print("Info Data ", info_data)
    return render(request, 'mainApp/courseList.html', {'info_data': info_data})

# views.py


# views.py

def student_view(request):
    all_students = Student.objects.all()
    info_data = []

    for student in all_students:
        student_info = {}
        student_info['id'] = student.id
        student_info['name'] = student.name
        student_info['courses'] = [course.title for course in student.courseinfo_set.all()]
        info_data.append(student_info)
    print("Student", info_data)
    return render(request, 'mainApp/student.html', {'info_data': info_data})


