from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime

from .models import Locker, Admin
"""
MATTS CODE IS COMMENTED OUT
THE FILES ARE ONLY ON THE PI

import sys
sys.path.append('/home/pi/libnfc/libnfc-1.7.0/examples')
from testCall import getCardUID
"""

def HomepageView(request):
    """
    the home page view (ILSA)
    """
    return render(request, 'ILSA/homepage.html')

def LockersView(request):
    """
    Grab all the lockers in the database
    pass the lockers and the card number to page
    """
    lockers = Locker.objects.all()
    swiped_card = request.session.get('card')
    context = {
        'locker_list': lockers,
        'swiped_card': swiped_card,
    }
    return render(request, 'ILSA/lockers.html', context)

@csrf_exempt
def swipe(request, card_uid):
    """
    MATTS CODE IS COMMENTED OUT
    THE FILES ARE ONLY ON THE PI
    function called when a card is swiped
    checks for the card value in the admin table first, directs to admin login if found
    then checks if the card is already being used, if in use flags the locker for unlock
    and removes the card uid from the locker
    """

    swiped_card_number = card_uid
    if Admin.objects.filter(admin_uid=swiped_card_number).exists():
        return JsonResponse({'response': 'admin'})
    elif Locker.objects.filter(card_uid=swiped_card_number).exists():
        locker = Locker.objects.get(card_uid=swiped_card_number)
        locker.card_uid = '0'
        locker.check_out_time = datetime.datetime.now().strftime('%H:%M:%S')
        locker.unlockable = True
        locker.save()

        request.session['locker_number'] = locker.lock_num
        request.session['check_out_flag'] = True
        request.session.modified = True

        return JsonResponse({'response': 'success'})



    """card wasn't in database, let user choose which locker to check into"""
    
    request.session['card'] = swiped_card_number
    request.session.modified = True

    return JsonResponse({'response': 'lockers'})

@csrf_exempt
def NFC(request):
    """
    card = getCardUID()
    if card == 'No Swipe':
        return HttpResponse('No Swipe')
    elif card == 'Error':
        return HttpResponse('Error')
    else:
        return HttpResponse(card)
"""

def check_in(request, lock_num):
    """
    get the chosen locker and check it out to the swiped card
    """
    if Locker.objects.filter(lock_num=lock_num).exists():
        locker = Locker.objects.get(lock_num=lock_num)
        request.session['locker_number'] = locker.lock_num
        request.session['check_out_flag'] = False
        request.session.modified = True

        locker.card_uid = request.session.get('card')
        locker.check_out_time = datetime.datetime.now().strftime('%H:%M:%S')
        locker.status = 'Taken'
        locker.unlockable = True
        locker.save()
        return redirect('ILSA:success')
    else:
        return redirect('ILSA')

def arduino(request, mac_address, battery_level):
    """
    Arduino logic for Django server
    :param mac_address: The mac address for the locker's ESP8266
    :param battery_level: The battery level of the locker's battery
    :return:
    """
    if Locker.objects.filter(mac_addr=mac_address).exists():
        locker = Locker.objects.get(mac_addr=mac_address)
        """The locker's battery is low, set it to sleep"""
        if locker.status == 'Low_Battery':
            return HttpResponse("Sleep")
        locker.battery_level = battery_level
        """Has the locker been flagged as unlockable?"""
        if locker.unlockable:
            if locker.card_uid != '0':
                """Locker is flagged and there is a card uid set, so the locker is being checked in"""
                locker.unlockable = False
                locker.save()
                return HttpResponse("Unlock")
            else:
                """Locker is flagged and there is no card uid set, so the locker is being checked out"""
                locker.unlockable = False
                locker.status = 'Open'
                """But if the battery is low, we don't want the locker to be available anymore"""
                if battery_level < 50:
                    locker.status = 'Low_Battery'
                locker.save()
                return HttpResponse("Unlock")
        else:
            return HttpResponse("Lock")
    else:
        return HttpResponse("No Locker")


def success(request):
    """
    A locker has been successfully checked out or a locker has been freed
    """
    check_out_flag = request.session.get('check_out_flag')
    lock_number = request.session.get('locker_number')
    context = {
        'lock_num': lock_number,
        'flag': check_out_flag,
    }
    return render(request, 'ILSA/success.html', context)

def swipetest(request):
    """
    testing swipe function
    """
    swiped_card_number = 'TEST Swipe'
    print('swipe test')
    """If the card uid is in the admin table, redirect to admin login"""
    if Admin.objects.filter(admin_uid=swiped_card_number).exists():
        return redirect(reverse('admin:index'))
    elif Locker.objects.filter(card_uid=swiped_card_number).exists():
        """The card uid is already in the database, so were checking out of that locker"""
        locker = Locker.objects.get(card_uid=swiped_card_number)
        locker.card_uid = '0'
        locker.check_out_time = datetime.datetime.now().strftime('%H:%M:%S')
        locker.unlockable = True
        locker.save()

        request.session['locker_number'] = locker.lock_num
        request.session['check_out_flag'] = True
        request.session.modified = True

        return redirect('ILSA:success')

    """Card wasn't in either database so pass the card uid to the locker view"""
    request.session['card'] = swiped_card_number
    request.session.modified = True

    return redirect('ILSA:lockers')
