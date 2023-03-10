from django.urls import path

from wow.views import index, PlayableRaceListView

urlpatterns = [
    path("", index, name="index"),
    path("playable_races/", PlayableRaceListView.as_view(), name="playable-race-list"),
    ]

app_name = "wow"
