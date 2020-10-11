from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, page):
    print("ENTRY DEFINITION RUNNING")
    return HttpResponse(markdown2.markdown(util.get_entry(page)))

def search(request):
    query = request.GET.get('q', '')
    print(f" THIS IS REQUEST GET {query} ")
    print(f"THIS IS LIST_ENTRIES {util.list_entries()}")
    if query in util.list_entries():
        return redirect(f"/wiki/{ query }")
    


