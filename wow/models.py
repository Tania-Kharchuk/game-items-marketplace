from django.contrib.auth.models import AbstractUser
from django.db import models


class PlayableRace(models.Model):
    name = models.CharField(max_length=255)
    faction = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlayableClass(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Gamer(AbstractUser):
    playable_race = models.ForeignKey(
        PlayableRace,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    playable_class = models.ForeignKey(
        PlayableClass,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.username} ({self.playable_race} {self.playable_class})"


class ItemType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class InteractionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name="items")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    interaction_type = models.ForeignKey(
        InteractionType,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        ordering = ["-created_at"]
