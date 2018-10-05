from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class WebsiteForm(forms.Form):
    entry = forms.CharField()