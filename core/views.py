from django.http import response
from django.shortcuts import render
import requests

def country_list(request):
	response = requests.get("https://restcountries.eu/rest/v2/all").json()
	context = {'response':response}
	return render(request, 'country_list.html', context)

