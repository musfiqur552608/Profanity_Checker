from rest_framework import serializers
from .models import Profanity

class ProfanitySerializer(serializers.Serializer):
    ctext = serializers.CharField(max_length=1000000)
    final = serializers.CharField(max_length=1000000)
    value = serializers.CharField(max_length=100)
    
    # created this function for create, read, delete
    def create(self, validated_data):
        return Profanity.objects.create(**validated_data)
    
    # created this function for update
    def update(self, instance, validated_data):
        instance.ctext = validated_data.get('ctext', instance.ctext)
        instance.final = validated_data.get('final', instance.final)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance