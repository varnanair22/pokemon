from django.http import HttpResponse
from django.shortcuts import render
from .models import pokemon
import requests

# Create your views here.


#def add_pokemon(request):
#    if request.method =="POST":
#        if request.POST.get('name') and request.POST.get('url'):
#            pokemon_inst = pokemon()
#            if pokemon.objects.all().filter(name__icontains=request.POST.get('name')).exists():
#                return HttpResponse("Pokemon with same name already existing!!!!")
#            else:
#                pokemon_inst.name = request.POST.get('name')
#                pokemon_inst.url = request.POST.get('url')
#                pokemon_inst.save()
#                return HttpResponse("Successfully added!!!!")
#        else:
#            return HttpResponse("Parameters missing!!!!")
#    else:
#        return render(request, 'add_pokemon.html')


def add_pokemon(request):
    if request.method == "POST":
        api = request.POST.get('api')
        response = requests.get(api)
        data = response.json()
        pokemons_lst = data['results']

        for i in pokemons_lst:
            if not pokemon.objects.all().filter(name__icontains=i['name']).exists():
                pokemon_data = pokemon(
                    name=i['name'],
                    url=i['url'],
                )
                pokemon_data.save()
        return HttpResponse("Successfully added!!!!")
    else:
        return render(request, 'add_pokemon_api.html')


def get_pokemon(request):
    pokemons = pokemon.objects.all()
    return render(request, 'pokemon.html',{'pokemons':pokemons})

