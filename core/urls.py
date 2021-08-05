from django.urls import path

from .views import country_list

urlpatterns = [
	path('', country_list, name='country_list')
]