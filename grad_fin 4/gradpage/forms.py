from django import forms
from .models import Archive

class ArchiveForm(forms.ModelForm):
    class Meta:
        model =  Archive
        fields = ['title', 'team_member', 'major','image','team_name','description']  # 필요한 필드를 선택