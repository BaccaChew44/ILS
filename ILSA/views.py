from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Locker

def HomepageView(request):
    return render(request, 'ILSA/homepage.html')


class LockersView(generic.ListView):
    template_name = 'ILSA/lockers.html'
    context_object_name = 'locker_list'

    def get_queryset(self):
        return Locker.objects.all()

def swipe(request, card_id):
    return HttpResponseRedirect('/lockers/')