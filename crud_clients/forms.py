from django import forms  
from .models import Customer,City
class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer  
        fields = ['name', 'contact', 'email','date_attention','time_attention',
'final_attention_time', 'company' ,'city', 'affair', 'response', 'date_of_request'
        ] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        ciudades = City.objects.all()
        a = [(i.id,i.name) for i in ciudades]
        CHOICES = tuple(a)
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'date_attention': forms.DateInput(attrs={ 'class': 'form-control' }),
            'time_attention': forms.TimeInput(attrs={ 'type':'time'}),
            'final_attention_time': forms.TimeInput(attrs={'type':'time'}),
            'company': forms.TextInput(attrs={ 'class': 'form-control' }),
            #'city': forms.TextInput(attrs={ 'class': 'form-control' }),
            'city' : forms.TypedChoiceField(choices=CHOICES, coerce=str),
            'affair': forms.TextInput(attrs={ 'class': 'form-control' }),
            'response': forms.TextInput(attrs={ 'class': 'form-control' }),
            'date_of_request': forms.DateInput(attrs={ 'class': 'form-control' }),
      }
