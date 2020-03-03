from rest_framework import serializers
from MembersServiceApp.models import MembersModel


class MembersSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MembersModel
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id')
