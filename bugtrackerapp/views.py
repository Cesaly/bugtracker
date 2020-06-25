from django.shortcuts import render, reverse, HttpResponseRedirect
from bugtrackerapp.forms import Login
from bugtrackerapp.models import Ticket, MyUser
from bugtrackerapp.forms import Ticketadd, Edit, Adduser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout


def index(request):
    html = 'index.html'

    # ticket = Ticket.objects.all()
    inprogress = Ticket.objects.filter(ticket_status=Ticket.INP)
    invalid = Ticket.objects.filter(ticket_status=Ticket.IN)
    new = Ticket.objects.filter(ticket_status='New')
    finished = Ticket.objects.filter(ticket_status=Ticket.F)
    print(Ticket.objects.get(title='add this'))
    # breakpoint()

    return render(request, html, {
        'inprogress': inprogress,
        'invalid': invalid,
        'new': new,
        'finished': finished})


@login_required
def authorslist(request):
    html = 'authorslist.html'
    authors = MyUser.objects.all()
    return render(request, html, {'authors': authors})


@login_required
def authorsview(request, id):
    html = 'authorsview.html'
    name = MyUser.objects.filter(id=id)
    tickets = Ticket.objects.all()
    working = tickets.filter(ticket_assignee=id)
    filed = tickets.filter(author=id)
    finished = tickets.filter(ticket_finisher=id)

    return HttpResponseRedirect(request, html, {
        'name': name, 'working': working,
        'filed': filed,
        'finished': finished})


@login_required
def info(request, id):
    html = "ticketinfo.html"
    detail = Ticket.objects.filter(id=id)
    return render(request, html, {'data': detail})


@login_required
def addticket(request):
    form = None
    html = "addticket.html"

    if request.method == 'POST':
        form = Ticketadd(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                author=request.user,
                description=data['description'],
            )
            return render(request, 'completed.html')
    else:
        form = Ticketadd()
    return render(request, html, {"form": form})


@login_required
def register(request):
    form = None
    html = "adduser.html"

    if request.method == "POST":
        form = Adduser(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create(
                username=data['username'],
                password=data['password']
            )
        return render(request, 'completed.html')
    else:
        form = Adduser()
    return render(request, html, {"form": form})


@login_required
def editticket(request, id):
    form = None
    html = 'editticket.html'
    instance = Ticket.objects.get(pk=id)
    if request.method == "POST":
        form = Edit(request.POST, instance=instance)

        if form.is_valid():
            form.save()
        return reverse('/')
    else:
        form = Edit(instance=instance)
        return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return reverse('/')


def login(request):
    html = 'login.html'
    form = Login()
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password'])
            print(user)
            if user:
                dj_login(request, user)
            return HttpResponseRedirect(request.GET.get('next', 'homepage'))
    return render(request, html, {'form': form})


@login_required
def inprogress(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.ticket_status = "ip"
    ticket.ticket_assignee = request.user
    ticket.ticket_finisher = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=(id,)))


@login_required
def invalid(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.ticket_status = "iv"
    ticket.ticket_assignee = None
    ticket.ticket_finisher = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=(id,)))


@login_required
def finished(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.ticket_status = "f"
    ticket.ticket_finisher = ticket.ticket_assignee
    ticket.ticket_assignee = None
    ticket.save()
    return HttpResponseRedirect(reverse('homepage'))
