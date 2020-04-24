from django.contrib.auth.forms import *
from FirstPage.models import Attractions


class CreateAttractionForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Название')
    address = forms.CharField(max_length=100, label='Адрес')
    descriptions = forms.CharField(max_length=300, label='Описание')
    city_name = forms.CharField(max_length=20, label='Город')
    options = (('Архитектура и памятники', 'Архитектура и памятники'),
               ('Религиозные объекты', 'Религиозные объекты'),
               ('Природные объекты', 'Природные объекты'),
               ('Исторические объекты', 'Исторические объекты'),
               ('Развлекательные объекты', 'Развлекательные объекты'),
               ('Музеи', 'Музеи'))
    type = forms.ChoiceField(choices=options)
    photo = forms.FileField(widget=forms.FileInput)

    class Meta:
        model = Attractions
        fields = ('name', 'address', 'descriptions', 'city_name', 'type', 'photo')
