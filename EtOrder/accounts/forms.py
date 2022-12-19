from django import forms
from django.contrib.auth.models import User
from accounts.models import Customer,Staff

class customerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']

BRANCH_CHOICES = (
    ('COMPS','COMPS'),
    ('IT','IT'),
    ('EXTC','EXTC')
)
class customerAddForm(forms.ModelForm):
    branch=forms.CharField(widget=forms.Select(choices=BRANCH_CHOICES))
    class Meta():
        model=Customer
        fields=['idno','branch']

class staffForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']

SUBJECT_CHOICES=(
    ('DS','Data Structures'),
    ('DLD','Digital Logic Design'),
    ('DM','Discrete Mathematics'),
    ('LA','Linear Algebra')
)

class staffAddForm(forms.ModelForm):
    subject=forms.CharField(widget=forms.Select(choices=SUBJECT_CHOICES))
    class Meta():
        model=Staff
        fields=['subject','phone']


        
