from django.views import View
from django.shortcuts import render, redirect
from . import my_functions , my_objects



def title_name(the_name: str):
    return the_name.lower()




class HomePageView(View):
    def get(self, request):

        my_name = "DANIEL"
        new_name = title_name(my_name)
        the_names = ['MATT','Louis','MJOE']
        other_names = the_names
        new_names = [x.title() for x in the_names]
        the_names.append('Tim')
        car1 = my_objects.car('green', 'honk honk')
        car2 = my_objects.car('blue', 'beep beep')
        car2.make = "Toyota"

        the_context={{'hi':'hello class!',
                      'name':new_name,
                      'names_list':new_names,
                      'car1':car1,
                      'car2':car2}}
        return render(request,'my_app/index.html',the_context)
