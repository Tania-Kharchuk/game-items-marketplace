from django.urls import path

from wow.views import index, PlayableRaceListView, PlayableClassListView



urlpatterns = [
    path("", index, name="index"),
    path("playable_races/", PlayableRaceListView.as_view(), name="playable-race-list"),
    path("playable_classes/", PlayableClassListView.as_view(), name="playable-class-list"),
    ]

app_name = "wow"
