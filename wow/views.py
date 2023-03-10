from django.shortcuts import render
from django.views import generic

from wow.models import Gamer, Item, ItemType, PlayableRace


def index(request):
    """View function for the home page of the site."""

    num_gamers = Gamer.objects.count()
    num_items = Item.objects.count()
    num_item_types = ItemType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_gamers": num_gamers,
        "num_items": num_items,
        "num_item_types": num_item_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "wow/index.html", context=context)


class PlayableRaceListView(generic.ListView):
    model = PlayableRace
    context_object_name = "playable_race_list"
    template_name = "wow/playable_race_list.html"
    paginate_by = 10
