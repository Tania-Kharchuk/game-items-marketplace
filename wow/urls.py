from django.urls import path

from wow.views import (index,
                       PlayableRaceListView,
                       PlayableClassListView,
                       ItemTypeListView,
                       InteractionTypeListView,
                       ItemListView,
                       GamerListView,
                       ItemDetailView,
                       GamerDetailView,
                       GamerCreateView,
                       GamerPlayableRaceClassUpdateView)


urlpatterns = [
    path("", index, name="index"),
    path("playable_races/", PlayableRaceListView.as_view(), name="playable-race-list"),
    path("playable_classes/", PlayableClassListView.as_view(), name="playable-class-list"),
    path("item_types/", ItemTypeListView.as_view(), name="item-type-list"),
    path("interaction_types/", InteractionTypeListView.as_view(), name="interaction-type-list"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("gamers/", GamerListView.as_view(), name="gamer-list"),
    path("gamers/<int:pk>/", GamerDetailView.as_view(), name="gamer-detail"),
    path("gamers/create/", GamerCreateView.as_view(), name="gamer-create"),
    path("gamers/<int:pk>/update", GamerPlayableRaceClassUpdateView.as_view(), name="gamer-update"),
    ]

app_name = "wow"
