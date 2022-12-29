from rest_framework import serializers

from ads.models.selected import Selected


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selected
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selected
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selected
        fields = '__all__'
