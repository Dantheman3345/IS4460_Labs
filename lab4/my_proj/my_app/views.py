from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def fix_name(name:str):
    new_name = name.title()
    return new_name

class HomePageView(View):
    def get(self, request):

        orig_name = 'jACOB'
        name = fix_name(orig_name)
        names = ['Luis','GabrIELA', 'MaRy', orig_name]

        fixed_names = my_functions.fix_names_list(names)

        car1 = my_objects.Car(make='Toyota,', model='Corolla,', year=2020, color='blue,', sound='honk honk')
        car2 = my_objects.Car(make='Honda,', model='Civic,', year=2019, color='red,', sound='beep beep')
        motorcycle1 = my_objects.Motorcycle(make="Harley,", model='fast,',year = 2029,color='is speed a color,',sound='vroom')

        context = {'hi':'hello world!',
                   'name':name,
                   "orig_name":orig_name,
                   'names' : names,
                   'fixed_names' : fixed_names,
                   'car1' : car1,
                   'car2' : car2,
                   'motorcycle1':motorcycle1
                   }

        return render(request, 'my_app/index.html',context)