from django.db import models


class Game(models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Playing', 'Playing'),
        ('Finished', 'Finished'),
    ]

    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planned')
    hours_played = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.platform}) – {self.status}"

    class Meta:
        ordering = ['title']
