from django import forms
from .models import UserRegisterModel
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from datetime import date

class UserRegisterForm(forms.ModelForm): 
    Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))  
    DOB = forms.DateField(required=True, widget=forms.DateInput(attrs={'class':'form-control', 'id':'datepicker1'}))  
    Email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))  
    Phone_number = forms.CharField(required=True, widget=PhoneNumberPrefixWidget(attrs={'class':'form-control'}, initial='IN'))  
   
    def clean_DOB(self):
        dob = self.cleaned_data['DOB']
        age = (date.today() - dob).days/365
        if age < 18 :
            raise forms.ValidationError('age must be greater then 18 years old to register')
        return dob
    class Meta:
        model = UserRegisterModel
        fields = '__all__'
