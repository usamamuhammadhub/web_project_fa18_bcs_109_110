from django.forms import fields
from django.forms import widgets
from app.models import Customer, OrderPlaced,Services, contact_us
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import PasswordInput, TextInput, Widget
from django.contrib.auth import password_validation
from django import forms
from django.core.exceptions import ValidationError
from PIL import Image
from django import forms
#from django.core.files.uploadedfile import SimpleUploadedFile





class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label=_("User Name"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             max_length=64, help_text='Enter a valid email address')

    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Confirm Password(again)"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
                               

    class Meta(UserCreationForm):
        model = User
        exclude = ('groups',)
        # fields = ("username","email","password1","password2")
        widgets ={'groups' : forms.HiddenInput(),
        }
        fields = ("username", "email", "password1", "password2","groups")
        sequence = fields


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class MypasswordChangeform(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}))


class Mypasswordrestform(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254,
                             widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))


class Mysetpasswordform(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'class': 'form-contorl'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': 'form-contorl'}),
    )



state_choice =(('National' ,'National') ,('International' ,'International'))
#FORM OF PROFILE
class CustomerForm(forms.ModelForm):
    customer_image1= forms.ImageField(label='Image')
    state= forms.ChoiceField(label='State',choices=state_choice)
   
    class Meta():
       model = Customer
 #fields = ("username","email","password1","password2"   "name",)
       fields = ("mobile","whatsapp_no" ,"phone_no","Address","city" ,"country","state", "customer_image1")
       widgets ={'Address' : forms.TextInput(attrs={'class':'form-control'}),
       'city' : forms.TextInput(attrs={'class':'form-control'}),
       'country' : forms.TextInput(attrs={'class':'form-control'}),
       'name' : forms.TextInput(attrs={'class':'form-control'}),
       'phone_no' : forms.TextInput(attrs={'class':'form-control'}),
       'mobile' : forms.TextInput(attrs={'class':'form-control'}),
       'whatsapp_no' : forms.TextInput(attrs={'class':'form-control'}),
       
   
       
       
       
       }
       sequence = fields

  



status_choice = (('Accepted', 'Accepted'), ('Call Me', 'Call Me'), ('Service is Start', 'Service is Start'),
                 ('Wait For Our Message', 'Wait For Our Message'), ('Service is Complete', 'Service is Complete'),
                 ('Cancel', 'Cancel'), ('Service is near to end', 'Service is near to end'),
                 ('This time is not Available', 'This time is not Available'),)  

#orderfrom
class Orderfrom(forms.ModelForm):
    status= forms.ChoiceField(label='Status',choices=status_choice)
    start_date =forms.DateTimeField()
    end_date =forms.DateTimeField()


    class Meta():
       model = OrderPlaced
 
       fields = ("status","start_date","end_date" ,"quantity","message")
       widgets ={
       'start_date' : forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }),
       'quantity' : forms.TextInput(attrs={'class':'form-control'}),
       'message' : forms.Textarea(attrs={'class':'form-control'})
       
       }
       sequence = fields

status_choice= (('read', 'read'), ('later', 'later'))
class contact_usform(forms.ModelForm):

     status= forms.ChoiceField(label='Status',choices=status_choice)
     class Meta():
       exclude = ('phone',)
       model = contact_us
       fields = ("status","phone")
       widgets ={'phone' : forms.HiddenInput()}
       sequence = fields
     
















cate= (('Day', 'Day'), ('Second', 'Second'), ('Minute', 'Minute'),
                    ('Square Fit', 'Square Fit'), ('Week', 'Week'), ('Year', 'Year'), ('Hour', 'Hour'),
                    ('Inch', 'Inch'), ('Centimeter', 'Centimeter'))



class Servicesform(forms.ModelForm):
   Service_image1= forms.ImageField(label='Image')
   Service_image2= forms.ImageField(label='Image')
   as_per= forms.ChoiceField(label='State',choices=cate)
   
   class Meta:
      model = Services
 
      fields = ['title','Actual_price','discounted_price','as_per','description','Service_image1','Service_image2']
      widgets ={
       'title' : forms.TextInput(attrs={'class':'form-control'}),
       'Actual_price' : forms.TextInput(attrs={'class':'form-control'}),
       'discounted_price' : forms.TextInput(attrs={'class':'form-control'}),
       'description' : forms.Textarea(attrs={'class':'form-control'}),
      }
      sequence = fields




