from django import forms
#from django_recaptcha.fields import ReCaptchaField




class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, widget=forms.TextInput)
    email = forms.EmailField(required=True, widget=forms.EmailInput)
    telefono = forms.CharField(max_length=15, required=True, widget=forms.TextInput)
    asunto = forms.CharField(max_length=200, required=True, widget=forms.TextInput)
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
    #captcha = ReCaptchaField()