from django.shortcuts import render

template = 'index.html'


# This method loads the main index html file
# and loads the root path.
def root_path(request):
    return render(request, template)


# This method loads the main index html file
# and loads any vue routes.
def vue_router(request):
    context = {}
    return render(request, template, context)
