from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Bunk, UserProfile
from .bunkForm import BunkForm

# Create your views here.

class IndexView(generic.ListView):
    model = Bunk
    template_name = 'bunker/index.html'
    context_object_name = 'bunk_list'

    def get_queryset(self):
        """
        Return a full list of recent bunk
        """
        return Bunk.objects.order_by('-time')
        # TODO:: only show some of most recent ones

#@login_required
class UserFeedView(generic.DetailView):
    model = UserProfile
    template_name = 'bunker/user_feed.html'
    context_object_name = 'usr'

    def get_queryset(self):
        return UserProfile.objects.all()


# For handling the form data
def add_bunk(request, user_id):
    if not request.user.is_authenticated():
        return render(request, '/bunker/registration/login.html')
    
    if request.method == "POST":
        form = BunkForm(request.POST)
        if form.is_valid():
            bunker = get_object_or_404(UserProfile, pk=user_id)
            try:
                b = Bunk()
                b.from_user = bunker
                b.to_user = UserProfile.objects.get(pk=request.POST['who_to_bunk'])
                b.time = timezone.now()
                b.save()
                return render(request, 'bunker/bunked.html', {
                    'user_name':b.to_user.user.username,
                    })
            except (KeyError, UserProfile.DoesNotExist):
                return render(request, 'bunker/add_bunk.html', {
                    'form':BunkForm(), 
                    'error':'Invalid User',
                    'user_id': user_id,
                    })
    else:
        form = BunkForm()
    return render(request, 'bunker/add_bunk.html', {
        'form':form,
        'user_id': user_id,
    })


# After submitting the form
def bunked(request):
    if not request.user.is_authenticated():
        return render(request, '/bunker/registration/login.html')

    return render(request, 'bunker/bunked.html')

# Logging out
def logout_view(request):
    logout(request)
    return render(request, 'bunker/loggedout.html')
