from rest_framework import serializers

from core.models import File


class GetCSVFileDataSerializer(serializers.ModelSerializer):
    __doc__ = "this serializer is used to return the data from file model"

    class Meta:
        model = File
        fields = "__all__"
