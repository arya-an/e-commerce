from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App.models import Product


class NewUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
        
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field_name in ('first_name','last_name','email','username','password1','password2'):
            self.fields[field_name].help_text = ''
            
            
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','strap_color','highlight','price','status']
        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'strap_color':forms.TextInput(attrs={'class':'form-control'}),
            'highlight':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }