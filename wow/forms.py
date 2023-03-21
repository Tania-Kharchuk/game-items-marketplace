from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator

from wow.models import Gamer, ItemType, Item


class GamerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name in ["username", "password1", "password2"]:
            self.fields[field_name].help_text = None

    class Meta(UserCreationForm.Meta):
        model = Gamer
        fields = UserCreationForm.Meta.fields


class GamerPlayableRaceClassUpdateForm(forms.ModelForm):
    class Meta:
        model = Gamer
        fields = ["playable_race", "playable_class"]


class PositiveDecimalFormField(forms.DecimalField):
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['min'] = 0
        return attrs


class ItemForm(forms.ModelForm):
    price = PositiveDecimalFormField(validators=[MinValueValidator(0)])

    class Meta:
        model = Item
        fields = ["name", "description", "price", "type", "interaction_type"]


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
