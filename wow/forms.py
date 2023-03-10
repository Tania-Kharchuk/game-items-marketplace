from django.contrib.auth.forms import UserCreationForm

from wow.models import Gamer


class GamerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Gamer
        fields = UserCreationForm.Meta.fields + (
            "playable_race",
            "playable_class"
        )
