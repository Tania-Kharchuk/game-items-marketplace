from django.urls import path

from wow.views import (index,
                       PlayableRaceListView,
                       PlayableClassListView,
                       ItemTypeCreateView,
                       ItemListView,
                       ItemCreateView,
                       ItemDetailView,
                       ItemUpdateView,
                       ItemDeleteView,
                       GamerListView,
                       GamerDetailView,
                       GamerCreateView,
                       GamerPlayableRaceClassUpdateView,
                       GamerDeleteView)


urlpatterns = [
    path("", index, name="index"),
    path(
        "playable_races/",
        PlayableRaceListView.as_view(),
        name="playable-race-list"
    ),
    path(
        "playable_classes/",
        PlayableClassListView.as_view(),
        name="playable-class-list"
    ),
    path(
        "item_types/create",
        ItemTypeCreateView.as_view(),
        name="item-type-create"
    ),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("items/create/", ItemCreateView.as_view(), name="item-create"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path(
        "items/<int:pk>/update/",
        ItemUpdateView.as_view(),
        name="item-update"
    ),
    path(
        "items/<int:pk>/delete/",
        ItemDeleteView.as_view(),
        name="item-delete"
    ),
    path("gamers/", GamerListView.as_view(), name="gamer-list"),
    path("gamers/<int:pk>/", GamerDetailView.as_view(), name="gamer-detail"),
    path("gamers/create/", GamerCreateView.as_view(), name="gamer-create"),
    path(
        "gamers/<int:pk>/update/",
        GamerPlayableRaceClassUpdateView.as_view(),
        name="gamer-update"
    ),
    path(
        "gamers/<int:pk>/delete/",
        GamerDeleteView.as_view(),
        name="gamer-delete"
    ),
    ]

app_name = "wow"
