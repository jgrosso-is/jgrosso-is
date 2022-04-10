import re

def filtro_vocales (cadena):
    return re.sub("[aeiouAEIOU]","",cadena)
def filtro_consonantes(cadena):
    return re.sub("[^aeiouAEIUO]","",cadena)

cadena = "Orange is the new BLACK"
x = ""
print("Filtro sin vocales: ", filtro_vocales(cadena))
print("Filtro sin consonantes: ", filtro_consonantes(cadena))