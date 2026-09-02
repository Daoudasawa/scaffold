from rest_framework import viewsets, permissions
from .models import HealthSchedule
from .serializers import HealthScheduleSerializer

class HealthScheduleViewSet(viewsets.ModelViewSet):
    queryset = HealthSchedule.objects.all()
    serializer_class = HealthScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Return schedules only for flocks owned by the user (RM6)
        user = self.request.user
        return HealthSchedule.objects.filter(flock__farm__owner=user)
