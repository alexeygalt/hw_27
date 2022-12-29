from rest_framework import serializers

from ads.models.location import Location
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)

        location, _ = Location.objects.get_or_create(name=self._location)
        user.location = location
        user.save()

        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        location, _ = Location.objects.get_or_create(name=self._location)
        user.location = location
        user.save()

        return user

    class Meta:
        model = User
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
