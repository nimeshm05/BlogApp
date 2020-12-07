from . import views as poll_views
from django.urls import path

urlpatterns = [
    path('', poll_views.home, name='poll_home'),
    path('create/', poll_views.create, name='poll_create'),
    path('vote/<int:poll_id>/', poll_views.vote, name='poll_vote'),
    path('result/<int:poll_id>/', poll_views.results, name='poll_results'),
    path('user_questions/', poll_views.user_questions, name='user_questions')
]