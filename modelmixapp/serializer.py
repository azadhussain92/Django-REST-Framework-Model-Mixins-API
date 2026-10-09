from rest_framework import serializers
from modelmixapp.models import userdata,status


class UserDataSerilizer(serializers.ModelSerializer):
    class Meta:
        model = userdata
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    User  = UserDataSerilizer(source="user", read_only=True)
    class Meta:
        model = status
        fields = "__all__"
