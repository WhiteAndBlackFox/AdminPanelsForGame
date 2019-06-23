from django import forms

from PanelsForGame.models import *

class PostPersonageDetail(forms.ModelForm):
    passwd = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = Personage
        fields = ('nick_name', 'fraction', 'kill_count', 'user', 'passwd', 'date_last_input', )

class PostProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'passwd', )

class PostInventory(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('personage', 'gObject', 'use_count', 'location_gObject' )

class PostPersonageTransfer(forms.ModelForm):
    class Meta:
        model = PersonageTransfer
        fields = ('personage', 'locations', 'date_last_visit', )
