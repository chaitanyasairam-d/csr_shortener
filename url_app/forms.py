from django import forms
from .models import UrlShortener
class NewShortLink(forms.ModelForm):
        url = forms.URLField(max_length=300,widget=forms.URLInput(
        attrs={
        'placeholder':'Enter URL',
        'class':'form-control'
        }
        ))
        shortcode = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Enter Your Own Shortcode or Leave Blank ',
        }
        ))
        def clean_shortcode(self):
            shortcode = self.cleaned_data['shortcode']
            sc_exists = UrlShortener.objects.filter(shortcode=shortcode).exists()
            if sc_exists:
                raise forms.ValidationError("Shortcode Already Exists!!!!!")
        class Meta():
            model = UrlShortener
            exclude = ['active']
