from django.urls import path

from . import views

urlpatterns = [
    # esim: /kyselyt/
    path("", views.index, name="index"),
    # esim: /kyselyt/5/
    path("<int:kysymys_id>/", views.näytä, name="näytä"),
    # esim: /kyselyt/5/tulokset/
    path("<int:question_id>/tulokset/", views.tulokset, name="tulokset"),
    # esim: /kysely/5/äänestä/
    path("<int:question_id>/äänestä/", views.äänestä, name="äänestä"),
]
