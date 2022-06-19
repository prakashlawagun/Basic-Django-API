from rest_framework import serializers
from .models import Student


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = '__all__'

    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value

    # def validate(self,data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #
    #     if nm.lower() == 'rohit' and ct.lower() != 'rachi':
    #         raise serializers.ValidationError('City must be Rachi')
    #     return data

    # read_only_fields = ['name','roll']
    # extra_kwargs = {'name':{'read_only':True}}
    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance
