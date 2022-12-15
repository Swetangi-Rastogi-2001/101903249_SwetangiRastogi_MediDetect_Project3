from django import forms
import datetime
from django.utils.text import slugify
import datetime


class InputDataForm(forms.Form):
    mdvp_fo_hz = forms.FloatField()
    mdvp_fhi_hz = forms.FloatField()
    mdvp_flo_hz = forms.FloatField()
    mdvp_jitter_per = forms.FloatField()
    mdvp_jitter_abs = forms.FloatField()
    mdvp_rap = forms.FloatField()
    mdvp_ppq = forms.FloatField()
    jitter_ddp = forms.FloatField()
    mdvp_shimmer = forms.FloatField()
    mdvp_shimmer_db = forms.FloatField()
    shimmer_apq3 = forms.FloatField()
    shimmer_apq5 = forms.FloatField()
    mdvp_apq = forms.FloatField()
    shimmer_dda = forms.FloatField()
    nhr = forms.FloatField()
    hnr = forms.FloatField()
    rpde = forms.FloatField()
    dfa = forms.FloatField()
    spread_1 = forms.FloatField()
    spread_2 = forms.FloatField()
    d2 = forms.FloatField()
    ppe = forms.FloatField()
    
