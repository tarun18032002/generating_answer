from django import forms

class UploadDocForm(forms.Form):
    file = forms.FileField()