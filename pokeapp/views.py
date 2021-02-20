from django.http import HttpResponse
from django.shortcuts import render
from .models import pokemon


# Create your views here.


def add_pokemon(request):
    if request.method =="POST":
        if request.POST.get('name') and request.POST.get('url'):
            pokemon_inst = pokemon()
            if pokemon.objects.all().filter(name__icontains=request.POST.get('name')).exists():
                return HttpResponse("Pokemon with same name already existing!!!!")
            else:
                pokemon_inst.name = request.POST.get('name')
                pokemon_inst.url = request.POST.get('url')
                pokemon_inst.save()
                return HttpResponse("Successfully added!!!!")
        else:
            return HttpResponse("Parameters missing!!!!")
    else:
        return render(request, 'add_pokemon.html')


def get_pokemon(request):
    pokemons = pokemon.objects.all()
    return render(request, 'pokemon.html',{'pokemons':pokemons})

