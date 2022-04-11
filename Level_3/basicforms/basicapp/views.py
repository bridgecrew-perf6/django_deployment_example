from django.shortcuts import render
from . import forms
# OR form basicapp import Forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
           form.save(commit=True)
           return form_name_view(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'basicapp/form_basic.html',{'form':form})