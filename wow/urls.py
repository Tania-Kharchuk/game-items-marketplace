from django.urls import path

from wow.views import index, PlayableRaceListView, PlayableClassListView, ItemTypeListView


urlpatterns = [
    path("", index, name="index"),
    path("playable_races/", PlayableRaceListView.as_view(), name="playable-race-list"),
    path("playable_classes/", PlayableClassListView.as_view(), name="playable-class-list"),
    path("item_types/", ItemTypeListView.as_view(), name="item-type-list"),
    ]

app_name = "wow"
