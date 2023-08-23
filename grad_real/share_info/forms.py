from django import forms
from .models import info

class infoForm(forms.ModelForm):
    class Meta:
        model = info
        fields = ['title', 'content', 'major']  # 필요한 필드를 선택