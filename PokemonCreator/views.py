from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Pokemon

class IndexView(generic.ListView):
    template_name = "PokemonCreator/index.html"
    context_object_name = "latest_pokemon_list"

    def get_queryset(self):
        """Return the last five created pokemon."""
        return Pokemon.objects.order_by("-creation_date")[:5]