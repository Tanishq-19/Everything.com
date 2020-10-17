from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    path("register", views.register, name="register"),
    path("form1", views.form1, name="form1"),
    path("form/Customer", views.form2, name="form2"),
    path("form/Seller", views.form3, name="form3"),
    path("Customer", views.customer_view, name="customer"),
    path("Seller", views.seller_view, name="seller"),
    path("chat/<str:name>", views.chat, name="chat"),
    path("chatslist", views.chatslist, name="chatslist"),
    path("chatinfo/<int:chat_id>", views.chatinfo, name="chatinfo"),
    path("orderinfo/<int:order_id>", views.orderinfo, name="orderinfo")

]