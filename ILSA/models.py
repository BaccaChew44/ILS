from django.db import models

class Locker(models.Model):
    lock_num = models.IntegerField()
    mac_addr = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    card_uid = models.CharField(max_length=200)
    check_out_time = models.TimeField('Time Checked Out')
    unlockable = models.BooleanField()


class Admin(models.Model):
    admin_uid = models.CharField(max_length=200)
