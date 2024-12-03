from rest_framework import serializers

from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "is_completed"]
        read_only_fields = ["id"]

    def validate(self, data):
        mission = self.context.get("mission")
        if mission and (mission.is_completed or data.get("is_completed", False)):
            raise serializers.ValidationError(
                "Cannot update notes on completed mission or target"
            )
        return data


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ["id", "spy_cat", "is_completed", "targets"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        targets_data = validated_data.pop("targets", [])

        if len(targets_data) < 1 or len(targets_data) > 3:
            raise serializers.ValidationError(
                "Mission must have between 1 and 3 targets"
            )

        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)

        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop("targets", None)

        instance.is_completed = validated_data.get(
            "is_completed", instance.is_completed
        )

        if targets_data is not None:
            instance.targets.all().delete()

            for target_data in targets_data:
                Target.objects.create(mission=instance, **target_data)

        instance.save()
        return instance
