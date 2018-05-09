from rest_framework import serializers
from api.models import Biodigester

class BiodigesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodigester
        fields = ('id', 'water_flow', 'temperature', 'internal_pressure', 'ph', 'gas_production')
