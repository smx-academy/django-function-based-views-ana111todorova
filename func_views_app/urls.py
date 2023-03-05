from django.urls import path
from .views import hello_world, licni_podatoci,ime, ploshtina_perimetar, ime_post, paren

urlpatterns = [
    path("hello-world", hello_world),
    path("zbir", licni_podatoci),
    path("ime/", ime),
    path("ploshtina_perimetar/", ploshtina_perimetar),
    path("ime_post/", ime_post),
    path("paren/", paren),

]