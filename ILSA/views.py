from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from django.utils import timezone
import datetime

from .models import Locker, Admin

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

def swipe(request):
    """
    function called when a card is swiped
    checks for the card value in the admin table first, directs to admin login if found
    then checks if the card is already being used, if in use flags the locker for unlock
    and removes the card uid from the locker
    """
    swiped_card_number = 'C9 I8 L0'
    if Admin.objects.filter(admin_uid=swiped_card_number).exists():
        return redirect(reverse('admin:index'))
    elif Locker.objects.filter(card_uid=swiped_card_number).exists():
        locker = Locker.objects.get(card_uid=swiped_card_number)
        locker.card_uid = '0'
        locker.check_out_time = datetime.datetime.now().strftime('%H:%M:%S')
        locker.unlockable = True
        locker.save()

        request.session['locker_number'] = locker.lock_num
        request.session['check_out_flag'] = True
        request.session.modified = True

        return redirect('ILSA:success')

    """
    card wasn't in database, let user choose which locker to check into
    """
    request.session['card'] = swiped_card_number
    request.session.modified = True
    return redirect('ILSA:lockers')

def check_in(request):
    """
    get the chosen locker and check it out to the swiped card
    """
    chosen_locker = get_object_or_404(Locker, pk=request.POST['locker'])
    request.session['locker_number'] = chosen_locker.lock_num
    request.session['check_out_flag'] = False
    request.session.modified = True

    chosen_locker.card_uid = request.session.get('card')
    chosen_locker.check_out_time = datetime.datetime.now().strftime('%H:%M:%S')
    chosen_locker.status = 'Taken'
    chosen_locker.unlockable = True
    chosen_locker.save()

    return redirect('ILSA:success')

def arduino(request):
    """Starting view for Arduino communication"""

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
