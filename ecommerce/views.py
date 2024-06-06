from django.shortcuts import render  # Importing the render function to render templates.


# Defining the index view function which handles requests to the home page.
def index(request):
    # The render function takes the request object, the template name, and an optional context dictionary.
    return render(request, 'index.html')
