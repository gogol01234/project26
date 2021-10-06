from django import forms
from app1.models import *
class Form1(forms.ModelForm):
    class Meta:
        model = Model2
        fields = ["name",  "email", "messages"]
        widgets = {"name":forms.TextInput(attrs = {"class":"form-control"}),
        "email":forms.EmailInput(attrs = {"class":"form-control"}),
        "messages":forms.Textarea(attrs = {"class":"form-control"})
        }