import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Locker, Admin

def make_locker(lock_num, mac_addr):
    """
    Helper function that makes a locker object
    :param lock_num: the locker number for the locker
    :param mac_addr: mac address for the locker
    :return:
    """
    return Locker.objects.create(lock_num=lock_num, mac_addr=mac_addr)

def make_admin(admin_name, admin_uid):
    """
    Helper function that makes a admin object
    :param admin_name: then name for the admin
    :param admin_uid:  the card uid for the admins card
    :return:
    """
    return Admin.objects.create(name=admin_name, admin_uid=admin_uid)

class LockerViewTests(TestCase):

    def test_no_lockers(self):
        """
        If there isn't any lockers, display that
        """
        response = self.client.get(reverse('ILSA:lockers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No lockers are configured.")

    def test_one_locker(self):
        """
        Make a locker and check if its passed to the page
        """
        make_locker(lock_num=1, mac_addr='102.0.0.7')
        response = self.client.get(reverse('ILSA:lockers'))
        self.assertQuerysetEqual(
            response.context['locker_list'],
            ['<Locker: 1>']
        )

    def test_two_lockers(self):
        """
        Make two lockers and check if both are passed to the page
        locker page can list multiple lockers
        """
        make_locker(lock_num=1, mac_addr='102.0.0.7')
        make_locker(lock_num=5, mac_addr='103.0.0.7')
        response = self.client.get(reverse('ILSA:lockers'))
        self.assertQuerysetEqual(
            response.context['locker_list'],
            ['<Locker: 1>', '<Locker: 5>'],
            ordered=False
        )

