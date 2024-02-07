from django.views import View
from django.shortcuts import render, redirect
from . import my_functions , my_objects

class HomePageView(View):

    @staticmethod
    def fix_name(name:str):
        new_name = name.title()
        return new_name

    def get(self, request):
        orig_name = 'jaCOB'
        name = fix_name(orig_name)
        
        names = ['Luis', 'GAbriella','Mary']
    
        context = {'hi':'hello world!', 
                 'name' : name,
                 'orig_name': orig_name,
                 'names':names}
        return render(request, 'my_app/index.html',context)