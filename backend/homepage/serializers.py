from rest_framework import serializers
from .models import Messages, EmailIds

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields=("id","first_name","last_name","email_id","message_box")

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailIds
        fields=("email_id",)
