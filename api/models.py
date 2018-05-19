from django.db import models

class Biodigester(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    water_flow = models.FloatField(blank=True, default=None)
    temperature = models.FloatField(blank=True, default=None)
    internal_pressure = models.FloatField(blank=True, default=None)
    ph = models.FloatField(blank=True, default=None)
    gas_production = models.FloatField(blank=True, default=None)
    volume = models.FloatField(blank=True, default=None)

    class Meta:
        ordering = ('created',)
