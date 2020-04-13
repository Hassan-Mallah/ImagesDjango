from django import forms
from .models import *


class ImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImagesForm, self).__init__(*args, **kwargs)
        self.fields['img_url'].required = False
        self.fields['img'].required = False

    class Meta:
        model = Image
        fields = ['img', 'img_url']