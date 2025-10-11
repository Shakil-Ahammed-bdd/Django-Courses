from django import forms
from . models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    # fields = ['name' , 'bio']   #akhane nirdisto kore bola ace ami tader niye kaj korte cai
    # exclude = ['bio'] # akhane bio chara baki shob gular kaj korte cai