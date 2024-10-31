from django.urls import path
from djangoPort import views
from . import chatbot

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path("chatbot/", chatbot.chatbot, name="chatbot"), 
    path("contact/", views.contact, name="contact")
]