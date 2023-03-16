from django.contrib.auth.forms import UserCreationForm
from django import forms

from wow.models import Gamer, PlayableRace, PlayableClass, ItemType


class GamerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Gamer
        fields = UserCreationForm.Meta.fields


class GamerPlayableRaceClassUpdateForm(forms.ModelForm):
    class Meta:
        model = Gamer
        fields = ["playable_race", "playable_class"]


class ItemSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Name"})
    )
    type = forms.ChoiceField(
        choices=[("", "All")] + [(type.id, type.name) for type in ItemType.objects.all()],
        required=False,
        label="",
    )
    owner = forms.BooleanField(
        required=False,
        initial=False,
        label="Show only my items"
    )
    created_at = forms.ChoiceField(
        choices=(
            ("-created_at", "From latest to oldest"),
            ("created_at", "From oldest to latest"),
        ),
        required=False,
        label=""
    )
