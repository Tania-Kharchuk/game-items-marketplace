from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from wow.forms import GamerCreationForm, GamerPlayableRaceClassUpdateForm, ItemSearchForm, ItemForm
from wow.models import Gamer, Item, ItemType, PlayableRace, PlayableClass


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


class PlayableClassListView(generic.ListView):
    model = PlayableClass
    context_object_name = "playable_class_list"
    template_name = "wow/playable_class_list.html"


class ItemTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = ItemType
    fields = "__all__"
    template_name = "wow/item_type_form.html"
    success_url = reverse_lazy("wow:item-create")


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item
    context_object_name = "item_list"
    template_name = "wow/item_list.html"
    paginate_by = 10
    queryset = Item.objects.all().select_related("type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        type_id = self.request.GET.get("type", "")
        order_by = self.request.GET.get("created_at", "")
        context["search_form"] = ItemSearchForm(
            initial={"name": name,
                     "type": type_id,
                     "owner": bool(self.request.GET.get("owner")),
                     "created_at": order_by}
        )
        return context

    def get_queryset(self):
        form = ItemSearchForm(self.request.GET)

        if form.is_valid():
            queryset = self.queryset.filter(name__icontains=form.cleaned_data["name"])
            type_id = form.cleaned_data["type"]
            if type_id:
                queryset = queryset.filter(type_id=type_id)
            elif self.request.GET.get("owner"):
                queryset = queryset.filter(owner=self.request.user)
            order_by = form.cleaned_data.get("order_by")
            if order_by:
                queryset = queryset.order_by(order_by)
            return queryset

        return self.queryset


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item
    queryset = Item.objects.select_related("owner", "type", "interaction_type")


class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("wow:item-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Item
    fields = ["name", "description", "price", "type", "interaction_type"]
    success_url = reverse_lazy("wow:item-list")


class ItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Item
    success_url = reverse_lazy("wow:item-list")


class GamerListView(LoginRequiredMixin, generic.ListView):
    model = Gamer
    context_object_name = "gamer_list"
    template_name = "wow/gamer_list.html"
    paginate_by = 10
    queryset = Gamer.objects.select_related("playable_race", "playable_class")


class GamerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Gamer
    queryset = Gamer.objects.select_related("playable_race", "playable_class")


class GamerCreateView(generic.CreateView):
    model = Gamer
    form_class = GamerCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("wow:index")


class GamerPlayableRaceClassUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Gamer
    form_class = GamerPlayableRaceClassUpdateForm
    success_url = reverse_lazy("wow:gamer-list")


class GamerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Gamer
    success_url = reverse_lazy("wow:index")
