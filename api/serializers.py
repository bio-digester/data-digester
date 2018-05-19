from rest_framework import serializers
from api.models import Biodigester

class BiodigesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodigester
        fields = ('water_flow', 'temperature', 'internal_pressure', 'ph', 'volume', 'gas_production')
