from django.urls import path

from .views import homePageView, sendMessageView, deleteMessageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('send_message/', sendMessageView, name='send_message'),
    path('delete_message/', deleteMessageView, name='delete_message'),
]