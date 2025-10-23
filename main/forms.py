# forms.py
from django import forms
from .models import Article, DemoUser, CompanySize, BusinessArea

class DemoUserForm(forms.ModelForm):
    class Meta:
        model = DemoUser
        fields = ['phone', 'name', 'last_name', 'company_name', 'company_size', 'business_area']
        widgets = {
            'company_size': forms.Select(),
            'business_area': forms.Select(),
        }




class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'image']