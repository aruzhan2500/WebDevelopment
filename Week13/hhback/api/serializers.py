from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Company, Vacancy

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.desciption)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.city)
        instance.save()
        return instance

class CompanySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Company
        fields = '__all__'

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    salary = serializers.CharField()
    company = CompanySerializer()

    def create(self, validated_data):
        vacancy = Vacancy(**validated_data)
        vacancy.save()
        return vacancy

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.desciption)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.company = validated_data.get('company', instance.city)
        instance.save()
        return instance

class VacancySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    salary = serializers.CharField()
    company = CompanySerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'
