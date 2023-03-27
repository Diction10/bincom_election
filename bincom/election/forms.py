from django import forms
from .models import *
from django.forms import ModelForm


# create form for registration
class PUForm(ModelForm):
    class Meta:
        model = PUResult
        fields = ['pollingunit_uniqueid']

        # override field label
        labels = {
            'pollingunit_uniqueid': ('Polling Unit ID'),
        }


class LGForm(ModelForm):
    class Meta:
        model = LGAName
        fields = ['lga_name']

        # override field label
        labels = {
            'lga_name': ('LG Name'),
        }


class NewResultForm(ModelForm):
    class Meta:
        model = PUResult
        fields = '__all__'
        # fields = ['pollingunit_uniqueid', 'party_abbreviation', 'party_score']

        # override field label
        labels = {
            'pollingunit_uniqueid' : ('PU ID'),
            'party__abbreviation' : ('Party'),
            'party_score' : ('Number of Votes'),
            'entered_by_user' : ( 'Agent Name'),
            'date_entered' : ('Date'),
            'user_IPaddress' : ('IP Address')
        }




