from django import forms #forms可以自動把網頁跟程式生成出來
from .models import Diary 

class DiaryForm(forms.ModelForm): #繼承括號裡的
    class Meta:
        model = Diary