from rest_framework import serializers
from .models import HealthSchedule

class HealthScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthSchedule
        fields = [
            "id",
            "flock",
            "title",
            "description",
            "scheduled_date",
            "completed",
            "client_uuid",
            "sync_status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
