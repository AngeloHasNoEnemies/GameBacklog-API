from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'platform', 'status', 'hours_played']

    # ── Validation Rule 1: hours_played cannot be negative ──────────────────
    def validate_hours_played(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "hours_played cannot be negative."
            )
        return value

    # ── Validation Rule 2: Finished games must have hours_played > 0 ────────
    def validate(self, data):
        status = data.get('status', getattr(self.instance, 'status', None))
        hours = data.get('hours_played', getattr(self.instance, 'hours_played', 0))

        if status == 'Finished' and hours == 0:
            raise serializers.ValidationError(
                "A game marked as 'Finished' must have hours_played greater than 0."
            )
        return data
