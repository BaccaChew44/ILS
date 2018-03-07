from django.db import models
import datetime

class Locker(models.Model):
    OPEN = 'Open'
    TAKEN = 'Taken'
    LOW_BAT = 'Low_Battery'
    STATUS_CHOICES = (
        (OPEN, "Open"),
        (TAKEN, "Taken"),
        (LOW_BAT, "Low_Battery")
    )
    lock_num = models.IntegerField('Locker Number')
    mac_addr = models.CharField(max_length=100)
    status = models.CharField('Status', max_length=50, choices=STATUS_CHOICES, default=OPEN)
    card_uid = models.CharField(max_length=200, default='0')
    check_out_time = models.TimeField('Time Last Used', default=datetime.datetime.now().strftime('%H:%M:%S'))
    unlockable = models.BooleanField('Unlockable', default=False)
    battery_level = models.IntegerField('Battery Level', default=100)

    def __str__(self):
        return 'Locker: ' + str(self.lock_num)


class Admin(models.Model):
    name = models.CharField('Name', max_length=200)
    admin_uid = models.CharField('Admin Card UID', max_length=200)

    def __str__(self):
        return self.name
