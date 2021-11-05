from django import forms
 
class UserForm(forms.Form):
    previos = forms.IntegerField(label = "Предыдущее значение")
    now = forms.IntegerField(label = "Текущее значение")