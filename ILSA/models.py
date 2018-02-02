from django.db import models

class Locker(models.Model):
    lock_num = models.IntegerField()
    mac_addr = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Open')
    card_uid = models.CharField(max_length=200, default=None)
    check_out_time = models.TimeField('Time Checked Out', default=None)
    unlockable = models.BooleanField(default=False)


class Admin(models.Model):
    name = models.CharField(max_length=200)
    admin_uid = models.CharField(max_length=200)
