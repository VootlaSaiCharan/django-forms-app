from django import forms
from .models import Detail

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields='__all__'
       # exclude=['phno']
        # fields=['name','phno','email','addr']
        labels = {
            'phno': 'Phone Number',  # Corrected the syntax here
            'addr': 'Address'        # Corrected the syntax here
        }

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-handle','placeholder':'Enter ur name'}),
            'phno':forms.TextInput(attrs={'class':'form-handle','placeholder':'Enter ur phonenumber'}),
            'email':forms.EmailInput(attrs={'class':'form-handle','placeholder':'Enter ur email'}),
            'addr':forms.Textarea(attrs={'class':'form-handle','placeholder':'Enter ur address'}),
        }





# class DetailsForm(forms.Form):
#     name=forms.CharField(max_length=50,label="Full Name in Capitals",required=False)
#     phno=forms.CharField(max_length=50,label="Phone no",required=False)
#     email=forms.CharField(max_length=50,required=True)
#     addr=forms.CharField(max_length=50)
    
    # addr=forms.CharField(max_length=50,label="your current residing Address",required=False,disabled=True,  initial="India")