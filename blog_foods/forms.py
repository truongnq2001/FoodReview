from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption','image','summary','price','address','rate','description')
        widgets = {
            'caption': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'rate': forms.NumberInput(attrs={'class':'form-control','min':0,'max':10}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption','image','summary','price','address','rate','description')
        widgets = {
            'caption': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'rate': forms.NumberInput(attrs={'class':'form-control','min':0,'max':10}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }