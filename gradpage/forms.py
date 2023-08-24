from django import forms
from .models import Archive

class ArchiveForm(forms.ModelForm):
    class Meta:
        model =  Archive
        fields = ['exhibit_title', 'service_title', 'major', 'team_name', 'team_member', 'description', 'file']  # 필요한 필드를 선택