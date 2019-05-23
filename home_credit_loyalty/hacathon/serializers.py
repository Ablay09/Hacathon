from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
'''
class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_lenght=250)
    date = serializers.CharField(max_length=1000)
    expiredDate = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=1000)
    bonus = serializers.IntegerField(default=0)
    status = serializers.CharField(max_length=500)
    donePercent = serializers.IntegerField(default=0)


    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task


    def update(self, instance, validated_data):
        instance.title = validated_data('title', instance.title)
        instance.date = validated_data('date', instance.date)
        instance.expiredDate = validated_data('expiredDate', instance.expiredDate)
        instance.description = validated_data('description', instance.description)
        instance.bonus = validated_data('bonus', instance.bonus)
        instance.status = validated_data('status', instance.status)
        instance.donePercent = validated_data('donePercent', instance.donePercent)
        instance.save()
        return instance
    
'''
