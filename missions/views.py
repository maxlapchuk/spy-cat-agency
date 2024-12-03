from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SpyCat, Mission, Target
from .serializers import MissionSerializer, TargetSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.spy_cat:
            return Response(
                {"error": "Cannot delete a mission already assigned to a cat"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=["POST"])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get("cat_id")

        try:
            cat = SpyCat.objects.get(id=cat_id, is_available=True)
        except SpyCat.DoesNotExist:
            return Response(
                {"error": "Cat not found or not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Mission.objects.filter(cat=cat, is_completed=False).exists():
            return Response(
                {"error": "Cat is already assigned to an active mission"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        mission.cat = cat
        mission.save()
        cat.is_available = False
        cat.save()

        serializer = self.get_serializer(mission)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def update_target(self, request, pk=None):
        mission = self.get_object()
        target_id = request.data.get("target_id")

        try:
            target = Target.objects.get(id=target_id, mission=mission)
        except Target.DoesNotExist:
            return Response(
                {"error": "Target not found in this mission"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if mission.is_completed or target.is_completed:
            return Response(
                {"error": "Cannot update completed mission or target"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = TargetSerializer(
            target, data=request.data, partial=True, context={"mission": mission}
        )
        if serializer.is_valid():
            serializer.save()

            if mission.targets.filter(is_completed=False).count() == 0:
                mission.is_completed = True
                mission.save()

                if mission.cat:
                    mission.cat.is_available = True
                    mission.cat.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
