from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .models import User, Customer, Seller, Chat

# Create your views here.
def index(request):
	return render(request,'Everything/front.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            # return render(request, "Everything/form1.html")
            check1 = Customer.objects.filter(customer=user)
            check2 = Seller.objects.filter(seller=user)
            if not check1 and not check2:
                return HttpResponseRedirect(reverse("form1"))
            if not check1:
                return HttpResponseRedirect(reverse('seller'))
            if not check2:
                return HttpResponseRedirect(reverse('customer'))
        else:
            return render(request, "Everything/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Everything/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")

            # Ensure password matches confirmation
            password = request.POST.get("password")
            confirmation = request.POST.get("confirmation")
        except IntegrityError:
            return render(request, "network/login.html", {
                "message": "Username already taken."
            })
        if password != confirmation:
            return render(request, "network/login.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "network/login.html", {
                "message2": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse('form1'))
    else:
        return render(request, 'Everything/login.html')

@login_required
def form1(request):
    if request.method == 'POST':
        data = request.POST['form1']
        if data == 'Customer':
            return HttpResponseRedirect(reverse('form2'))
        else:
            return HttpResponseRedirect(reverse('form3'))
        # print(data)
        # return HttpResponseRedirect( data, reverse('form2'))
    return render(request, "Everything/form1.html")

@login_required
def form2(request):
    if request.method == 'POST':
        customer = request.user
        first = request.POST['first']
        last = request.POST['last']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zip']
        contact = request.POST['phone']

        new_customer = Customer(customer=customer, firstname=first, lastname=last, address=address, city=city, state=state, zipcode=zipcode, contact=contact)
        new_customer.save()
        return HttpResponseRedirect(reverse('customer'))
    return render(request, "Everything/form2.html")

@login_required
def form3(request):
    if request.method == 'POST':
        seller = request.user
        name = request.POST['name']
        shop = request.POST['shop']
        p_type = request.POST['type']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zip']
        contact = request.POST['phone']

        new_seller = Seller(seller=seller, fullname=name, shop=shop, p_type=p_type, address=address, city=city, state=state, zipcode=zipcode, contact=contact)
        new_seller.save()
        return HttpResponseRedirect(reverse('seller'))
    return render(request, "Everything/form3.html")

@login_required
def customer_view(request):
    #sellers = Seller.objects.all()
    return render(request, "Everything/index_customer.html",{
        'sellers': Seller.objects.all()
        })

@login_required
def seller_view(request):
    return render(request, "Everything/index_seller.html",{
        'chats':Chat.objects.filter(recipient=request.user)
        })

@login_required
def chat(request, name):
    if request.method == 'POST':
        chat = request.POST['chat']
        sender = request.user
        recipient = User.objects.get(username=name)
        chat = Chat(sender=sender, recipient=recipient, chat=chat)
        chat.save()
        return HttpResponseRedirect(reverse('chatslist'))
    return render(request, "Everything/chat.html", {
        'name': name
        })

@login_required
def chatslist(request):
    chatslist = Chat.objects.filter(sender=request.user)
    return render(request, "Everything/chatlist.html",{
        'chatslist': chatslist
        })

@login_required
def chatinfo(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    if request.method == 'POST':
        chat.finish = True
        chat.save()
        return HttpResponseRedirect(reverse('customer'))
    user = chat.recipient
    info = Seller.objects.get(seller=user)
    return render(request, "Everything/chatinfo.html",{
        'chat':chat,
        'info':info
        })

@login_required
def orderinfo(request, order_id):
    order = Chat.objects.get(id=order_id)
    if request.method == 'POST':
        totalprice = request.POST['total']
        order.takeaway = True
        order.total = totalprice
        order.save()
        return HttpResponseRedirect(reverse('seller'))
    user = order.sender
    info = Customer.objects.get(customer=user)
    return render(request, "Everything/orderinfo.html",{
        'order':order,
        'info':info
        })