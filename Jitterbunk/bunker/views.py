from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Bunk, UserProfile

# Create your views here.


class IndexView(generic.ListView):
    model = UserProfile
    template_name = 'bunker/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        """
        Return a full list of recent bunk
        """
        return UserProfile.objects.all()
        # TODO:: only show some of most recent ones


class UserFeedView(generic.DetailView):
    model = UserProfile
    template_name = 'bunker/user_feed.html'

    def get_queryset(self):
        return UserProfile.objects.all()
