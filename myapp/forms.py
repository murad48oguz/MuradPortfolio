from django import forms

from .models import Contact

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = [
            
            'name',
            'email',
            'subject',
            'message',
            
            
            
        ]
        
    
    
    
    
    
    
    
    
    
    
    
    # name = forms.CharField(label='Your name', max_length=127)
    # email = forms.EmailField(label = 'Email',max_length=100)
    # subject = forms.CharField(label='Subject', max_length=127)
    # message = forms.CharField(label = 'Message')

