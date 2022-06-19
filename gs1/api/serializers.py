from rest_framework import serializers
from .models import Student


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validation
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value
    # Object level validation

    # def validate(self,data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #
    #     if nm.lower() == 'rohit' and ct.lower() != 'rachi':
    #         raise serializers.ValidationError('City must be Rachi')
    #     return data
