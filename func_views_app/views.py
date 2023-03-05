from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#CBW - Class based Views

#FBW - Function based Views

@api_view(["GET"])
def hello_world(request):
    data= {"info":"dobredojdovte vo django"}
    return Response(data)


@api_view(["GET"])
def licni_podatoci(request):
    broj1 =5
    broj2= 10
    zbir = broj1+broj2
    data = {"info":"Zbirot na broevite e {}".format(zbir)}
    return Response(data)


#1. Funkcija koja prima GET i POST metodi. Vo body vo POST metodod da se praka ime / string. Funkcijata da vraka 
# json so slednive podatoci
#Imeto koe e prateno
#Dolzinata na Imeto
#Imeto so site golemi bukvi
#Imeto so site malite bukvi golemi, a golemite malite

@api_view(["GET"])
def ime(request):
    ime1 = request.GET["ime1"]
    dolzina= len(ime1)
    golemi= ime1.upper()
    golemi_mali= ime1.swapcase()

    print(ime1)
    data = {"info":"Dobredojdovte vo Django {}".format(ime1),
            "dolzina":"Imeto sodrzi {} bukvi".format(dolzina),
            "golemi" : golemi,
            "mali i golemi" : golemi_mali
             }
    return Response(data)


@api_view(["POST"])
def ime_post(request):
    print(request.method)
    ime1 = request.data.get("ime1", None)
    dolzina= len(ime1)
    golemi= ime1.upper()
    golemi_mali= ime1.swapcase()   

    print("Imeto e ", ime1)
    print("Dolzinata na imeto e  ", dolzina)
    print("So golemi bukvi  ", golemi)
    
    return Response({"info":"uspesno"})


#2.Funkcija koja ke prima POST metod. Funkcijata da moze da presmetuva plostina i perimetar na pravoagolnik. 
# Vo body da se prakjaat stranite i sto da se presmeta plostina ili perimetar. Funkcijata da vraka JSON so slednive podatoci
#strana a
#strana b
#plostina / perimetar(rezultatot)

@api_view(["POST"])
def ploshtina_perimetar(request):
    print(request.method)
    stranaa = request.data.get("stranaa")
    stranab = request.data.get("stranab")
    perimetar = 2*stranaa+2*stranab
    ploshtina = stranaa*stranab
    print("stranata a e {}".format(stranaa)) 
    print("stranata b e {}".format(stranab))
    print("Ploshtinata e {}".format(ploshtina))
    print("Perimetarot e {}".format(perimetar))
   
    return Response({"stanata a e": stranaa,
                     "stanata b e": stranab,
                     "Perimetarot e " : perimetar,
                     "Ploshtinata e " : ploshtina,
                     })




#3.Funkcija koja ke prima GET metod. Funkcijata da prima get parametar koj e 
# broj i da se proveri dali
#  toj broj e paren ili neparen. Da se vraka JSON so klucen zbor paren i 
# true / false vrednost

@api_view(["GET"])
def paren(request):
    broj = int(request.GET.get("broj", ""))

    if broj %2== 0:
        data = {"poraka": " {}  e paren".format(broj),
                        } 
        
    else :
        data = {"poraka": " {}  e neparen".format(broj)}

    return Response(data)