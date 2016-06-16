from django import forms 

from .models import UserProfile

class BunkForm(forms.Form):
    choices = [(profile.id, profile.user.username) for profile in UserProfile.objects.all()]
    who_to_bunk = forms.ChoiceField(choices=choices)
   
