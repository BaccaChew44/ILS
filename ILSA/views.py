from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse

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
    return redirect('ILSA:lockers')

def check_out(request):
    chosen_locker = get_object_or_404(Locker, pk=request.POST['locker'])
    print(chosen_locker.lock_num)
    return redirect(reverse('ILSA:home page'))


