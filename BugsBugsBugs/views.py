from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
    return HttpResponse("The Login page")


def logout_view(request):
    return HttpResponse("You Logged Out")
