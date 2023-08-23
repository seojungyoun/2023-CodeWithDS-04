from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'major']  # 필요한 필드를 선택