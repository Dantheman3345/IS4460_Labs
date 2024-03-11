# Movie/views.py

from django.shortcuts import render

def login_view(request):
    # Assuming your HTML file is named login.html and is placed inside a templates folder within the Movie app.
    return render(request, 'login.html', {'title': 'HW3 Movie App', 'name': 'Daniel Myers'})
