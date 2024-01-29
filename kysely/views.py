from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Heippatirallaa. olet kysely-apin index-sivulla.")
