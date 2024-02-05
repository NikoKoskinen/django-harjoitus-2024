from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render

from .models import Kysymys


def index(request):
    kysymyslista = Kysymys.objects.order_by("-julkaisupvm")[:2]
    context = {
        "kysymykset": kysymyslista,
    }
    return render(request, "kysely/index.html", context)


def näytä(request, kysymys_id):
   kysymys = get_object_or_404(Kysymys, pk=kysymys_id)
   return render(request, "kysely/näytä.html", {"kysymys": kysymys})


def tulokset(request, question_id):
    return HttpResponse(f"Katsot kysymyksen {question_id} tuloksia")


def äänestä(request, question_id):
    return HttpResponse(f"Olet äänestämässä kysymykseen {question_id}")