from django.shortcuts import render
from django.shortcuts import redirect

from .models import Locker

def HomepageView(request):
    return render(request, 'ILSA/homepage.html')


def LockersView(request):
    lockers = Locker.objects.all()
    swiped_card = request.session.get('card')
    context = {
        'locker_list': lockers,
        'swiped_card': swiped_card,
    }
    return render(request, 'ILSA/lockers.html', context)


def swipe(request):
    request.session['card'] = 'C9 I8 L0'
    request.session.modified = True
    print('Hello!')
    print(request.session['card'])
    return redirect('ILSA:lockers')
