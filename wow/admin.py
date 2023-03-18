from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from wow.models import (PlayableRace,
                        PlayableClass,
                        ItemType,
                        Item,
                        Gamer,
                        InteractionType)


@admin.register(Gamer)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "playable_race", "playable_class",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "playable_race",
                        "playable_class",
                    )
                }
            ),
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "playable_race",
                        "playable_class",
                    )
                },
            ),
        )
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("type",)


admin.site.register(PlayableRace)
admin.site.register(PlayableClass)
admin.site.register(ItemType)
admin.site.register(InteractionType)
