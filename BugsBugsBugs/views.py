from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from BugsBugsBugs.forms import LoginForm, NewTicketForm
from BugsBugsBugs.models import Ticket
from django.shortcuts import render


@login_required
def index(request):
    new = Ticket.objects.filter(status='NEW').order_by('date_Filed')
    in_progress = Ticket.objects.filter(status='In Progress').order_by('date_Filed')
    done = Ticket.objects.filter(status='Done').order_by('date_Filed')
    invalid = Ticket.objects.filter(status='Invalid').order_by('date_Filed')

    return render(request, 'index.html',
                  {
                      'new': new,
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def create_ticket_view(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                filed_By=request.user,
                title=data['title'],
                description=data['description'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = NewTicketForm()
    return render(request, 'form.html', {'form': form})


@login_required
def edit_ticket_view(request, ticket_id):
    instance = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = NewTicketForm(request.POST, initial={
            'title': instance.title,
            'description': instance.description
        })
        if form.is_valid():

            instance.title = form.cleaned_data['title']
            instance.description = form.cleaned_data['description']
            instance.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = NewTicketForm(initial={
        'title': instance.title,
        'description': instance.description
    })
    return render(request, 'form.html', {'form': form})


@login_required
def ticket_details_view(request, ticket_id):
    data = Ticket.objects.get(id=ticket_id)
    print(data)
    return render(request, 'details.html', {'ticket': data})
