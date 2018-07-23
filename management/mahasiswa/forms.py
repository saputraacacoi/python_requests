from django import forms
from orm.models import Mahasiswa

class MahasiswaForm(forms.Form):
    
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100)
    
    class Meta:
        model = Mahasiswa