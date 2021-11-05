from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Data
 
# получение данных из бд
def index(request):
	all_data = Data.objects.all()
	return render(request, "index.html", {"all_data": all_data})


	# сохранение данных в бд
def create(request):
	if request.method == "POST":
		pokaz = Data()
		pokaz.previos = request.POST.get("previos")
		pokaz.now = request.POST.get("now")
		pokaz.save()
	return HttpResponseRedirect("/")

