from rest_framework import serializers

from main.models import ToDo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ('user', )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
