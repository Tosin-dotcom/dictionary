from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import NewForm

import requests

# Create your views here.

    
languages = {
    'englishUS':'en_US',
    'hindi':'hi',
    'spanish':'es',
    'french':'fr',
    'japanese':'ja',
    'russian' : 'ru',
    'englishUK' : 'en_GB',
    'german' : 'de',
    'italian' : 'it',
    'korean' : 'ko',
    'brazilianPortuguese': 'pt-BR',
    'arabic' : 'ar',
    'turkish' : 'tr'
}



def home_view(request):
    context = {}
    form = NewForm(request.POST)
    
    if form.is_valid():
        subject = form.cleaned_data['search']
        data = form.cleaned_data['language']
        language = languages[data]
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/{language}/{subject}').json()
        context['response'] = response
        
    form = NewForm()
    context['form'] = form
    return render(request, 'home/home_page.html', context)



