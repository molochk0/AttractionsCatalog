from django.contrib.auth.forms import *
from FirstPage.models import Attractions, Attachment
from multiupload.fields import MultiMediaField
from django.core.validators import validate_image_file_extension


class CreateAttractionForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Название')
    city_name = forms.CharField(max_length=50, label='Город')
    address = forms.CharField(max_length=100, label='Адрес')
    descriptions = forms.CharField(max_length=300, label='Описание', widget=forms.Textarea(attrs={'rows': 4}))
    options = (('Архитектура и памятники', 'Архитектура и памятники'),
               ('Религиозные объекты', 'Религиозные объекты'),
               ('Природные объекты', 'Природные объекты'),
               ('Исторические объекты', 'Исторические объекты'),
               ('Развлекательные объекты', 'Развлекательные объекты'),
               ('Музеи', 'Музеи'))
    type = forms.ChoiceField(choices=options, label='Тип')

    class Meta:
        model = Attractions
        fields = ('name', 'city_name', 'address', 'descriptions',  'type')


class CreatePhotoAttachmentsForm(forms.ModelForm):
    photo = MultiMediaField(min_num=1, max_num=3, label='Фотографии', max_file_size=1024 * 1024 * 5, media_type='image', validators=[validate_image_file_extension])

    class Meta:
        model = Attachment
        fields = ('photo',)
