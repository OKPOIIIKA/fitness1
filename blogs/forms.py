from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput



class ArticlesForm(ModelForm):
   class Meta:
      model = Articles
      fields = ['title','anons','full_text','date']

      widgets = {
         'title': TextInput(attrs={
            'placeholder':'Название блога',
            'class':'list_of_forms forms1'
         }),
         'anons': TextInput(attrs={
            'placeholder':'Анонс блога',
            'class':'list_of_forms forms1'
         }),
         'full_text': Textarea(attrs={
            'placeholder':'Текст блога',
            'class':'list_of_forms'
         }),
         'date': DateTimeInput(attrs={
            'placeholder':'Дата публикации',
            'class':'list_of_forms forms1'
         }),
      }