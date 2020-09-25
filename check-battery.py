import time
import psutil as ps
from pynotifier import Notification
import power

while True:
    check_plug = power.PowerManagement().get_providing_power_source_type()
    battery_condition = ps.sensors_battery()
    percent = battery_condition.percent
    percent = round(percent, 2)

    if not check_plug:
        Notification(
            title='Notification Battery',
            description='Plugged into wall socket. {}'.format(
                str(percent))+"% left",
            icon_path='/home/kosia/Pulpit/battery.png',
            urgency=Notification.URGENCY_CRITICAL
        ).send()

    else:
        Notification(
            title='Notification Battery',
            description='On battery. {}'.format(str(percent))+"% left.",
            icon_path='/home/kosia/Pulpit/status.png',
            urgency=Notification.URGENCY_CRITICAL
        ).send()

    time.sleep(320)
