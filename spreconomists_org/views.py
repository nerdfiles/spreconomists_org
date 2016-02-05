from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response(
        'home.html',
        context_instance=RequestContext(request)
    )

def about(request):
    return render_to_response(
        'about.html',
        context_instance=RequestContext(request)
    )

def events(request):
    return render_to_response(
        'events.html',
        context_instance=RequestContext(request)
    )

def gallery(request):
    return render_to_response(
        'gallery.html',
        context_instance=RequestContext(request)
    )

def contact(request):
    return render_to_response(
        'contact.html',
        context_instance=RequestContext(request)
    )
