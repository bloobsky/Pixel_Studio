from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    fromwho = forms.CharField(required=True, label='Your name')
    subject = forms.CharField(required=True, label='subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Enter your message')
