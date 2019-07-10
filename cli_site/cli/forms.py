from django import forms 

class CLI(forms.Form):
    inputArea = forms.CharField(widget=forms.Textarea(), max_length=300)
