from rest_framework import viewsets, permissions
from .models import Recommendation
from .serializers import RecommendationSerializer
from apps.alerts.models import Alert

class RecommendationViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        alert_id = self.kwargs.get("alert_pk")
        # In a real app, we would add strict permission checking based on Alert -> Flock -> Farm Owner
        return Recommendation.objects.filter(alert_id=alert_id)

    def perform_create(self, serializer):
        alert_id = self.kwargs.get("alert_pk")
        alert = Alert.objects.get(id=alert_id)
        
        # Check if user is professional
        is_pro = self.request.user.role in ['veterinarian', 'technician']
        
        serializer.save(
            alert=alert, 
            generated_by=self.request.user.get_full_name() or self.request.user.email,
            validated_by_professional=is_pro
        )
