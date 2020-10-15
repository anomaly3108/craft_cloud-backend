from rest_framework import serializers
from CC_backend.models import testdata

class serializationclass(serializers.ModelSerializer):
    class Meta:
        model=testdata
        fields='__all__'