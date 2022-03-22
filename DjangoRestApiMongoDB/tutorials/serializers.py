from rest_framework import serializers
from tutorials.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    ''' Tutorial serializer '''

    class Meta:
        ''' Meta class '''

        model = Tutorial
        fields = (
            'id',
            'title',
            'description',
            'published'
        )
