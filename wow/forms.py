from django.contrib.auth.forms import UserCreationForm
from django import forms

from wow.models import Gamer, PlayableRace, PlayableClass


class GamerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Gamer
        fields = UserCreationForm.Meta.fields + (
            "playable_race",
            "playable_class"
        )


# class GamerCreationForm(UserCreationForm):
#     playable_race = forms.ModelChoiceField(
#         queryset=PlayableRace.objects.all(),
#         widget=forms.RadioSelect()
#     )
#     playable_class = forms.ModelChoiceField(
#         queryset=PlayableClass.objects.all(),
#         widget=forms.RadioSelect()
#     )
#
#     class Meta(UserCreationForm.Meta):
#         model = Gamer
#         fields = UserCreationForm.Meta.fields + (
#             "playable_race",
#             "playable_class"
#         )


class GamerPlayableRaceClassUpdateForm(forms.ModelForm):
    class Meta:
        model = Gamer
        fields = ["playable_race", "playable_class"]
