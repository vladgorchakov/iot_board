from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Monitoring, Sensors
from django.db.models import ObjectDoesNotExist
import datetime


def show_monitoring(requests):
    mon = Monitoring.objects.all()
    s = ''
    for m in mon:
        s += f'<p>{m.sensor} {m.date} {m.value}</p>'

    return HttpResponse(s)


def show_info(requests, mon_id):
    try:
        data = Monitoring.objects.get(pk=mon_id)
        return HttpResponse(str(data))

    except ObjectDoesNotExist:
        print('ex')
        return HttpResponseRedirect('/monitoring')

def take_info(requests):
    sensor = requests.GET.get("s", None)
    value = requests.GET.get("v", None)
    if value and sensor:
        date = datetime.datetime.now()
        print(date, sensor, value)
        sensor = Sensors.objects.filter(name=sensor.upper())
        print(sensor.sensorss_name)
        m = Monitoring(2, value=value, date=date)
        m.save()
        return HttpResponse('OK')
    else:
        return HttpResponse('Not data')
