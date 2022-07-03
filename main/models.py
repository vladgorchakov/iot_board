from django.db import models


class Sensors(models.Model):
    name = models.fields.CharField(max_length=20)
    type = models.fields.CharField(max_length=20)
    place = models.fields.CharField(max_length=20)
    description = models.fields.TextField()

    def __str__(self):
        return f'{self.name}-{self.pk}'


class Monitoring(models.Model):
    date = models.DateTimeField()
    sensor = models.ForeignKey(Sensors, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.FloatField()

    def __str__(self):
        return f'{self.date}: {self.sensor}'
