from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from BugsBugsBugs.forms import LoginForm
from BugsBugsBugs.models import Ticket
from django.shortcuts import render


@login_required
def index(request):
    new = Ticket.objects.filter(status='New').order_by('date_Filed')
    in_progress = Ticket.objects.filter(status='In Progress').order_by('date_Filed')
    done = Ticket.objects.filter(status='Done').order_by('date_Filed')
    invalid = Ticket.objects.filter(status='Invalid').order_by('date_Filed')

    return render(request, 'index.html',
                  {
                      'NEW': new,
                      'in_progress': in_progress,
                      'done': done,
                      'invalid': invalid
                  })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

