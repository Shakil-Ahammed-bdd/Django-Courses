from django import forms
from . models import Category

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'
    # fields = ['name' , 'bio']   #akhane nirdisto kore bola ace ami tader niye kaj korte cai
    # exclude = ['bio'] # akhane bio chara baki shob gular kaj korte cai