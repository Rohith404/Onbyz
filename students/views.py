from django.shortcuts import render, redirect
from .models import Students

def index(request):
    if request.method == "POST":
        search_value = request.POST.get('search_value')
        students = Students.objects.filter(Year_And_Month__icontains = search_value) | Students.objects.filter(Name__icontains = search_value)
    else:
        students = Students.objects.all()
    context = {'students' : students}
    return render(request, 'index.html', context)