from rest_framework.serializers import ModelSerializer
from .models import *


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone',
                  'address', 'date_of_birth']
        
        #fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance