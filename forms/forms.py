from django import forms
from django.core.validators import RegexValidator
from .models import Detail

class DetailsForm(forms.ModelForm):
    phno = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits.',
                code='invalid_phno'
            )
        ],
        widget=forms.TextInput(attrs={'class': 'form-handle', 'placeholder': 'Enter your phone number'})
    )

    class Meta:
        model = Detail
        fields = '__all__'
        labels = {
            'phno': 'Phone Number',
            'addr': 'Address'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-handle', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-handle', 'placeholder': 'Enter your email'}),
            'addr': forms.Textarea(attrs={'class': 'form-handle', 'placeholder': 'Enter your address'}),
        }