from django import forms
from .models import Info

class infoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'content', 'major']  # 필요한 필드를 선택