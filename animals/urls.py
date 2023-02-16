# -*- coding: utf-8 -*-
from django.urls import path

from animals.views import animals_list_view, animals_id_view
app_name="animals"
urlpatterns=[
    path("",animals_list_view, name = "a"),
    path("animals/<int:pk>", animals_id_view, name="animals"),
]
