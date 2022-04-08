from django import forms



    
TITLE_CHOICES = (
    ['englishUS', 'EnglishUS'],
    ['hindi', 'Hindi'],
    ['spanish', 'Spanish'],
    ['french', 'French'],
    ['japanese', 'Japanese'],
    ['russian', 'Russian'],
    ['englishUK', 'EnglishUK'],
    ['german', 'German'],
    ['italian', 'Italian'],
    ['korean', 'Korean'],
    ['brazilianPortuguese', 'BrazilianPortuguese'],
    ['arabic', 'Arabic'],
    ['turkish', 'Turkish']
)

class NewForm(forms.Form):
    language = forms.CharField(
        initial = TITLE_CHOICES[0],
        max_length=30,
        label=False,
        widget=forms.Select(choices=TITLE_CHOICES))
    search = forms.CharField(max_length=100, label=False, widget=forms.TextInput({ "placeholder": "Search here"}))
        

