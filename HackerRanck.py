import re

cadena = "AAWSWAWSSTAMOS READYAWSAWSAWS"

while re.search("AWS", cadena):
    cadena = re.sub("AWS","",cadena)
    if not cadena:
        cadena = "-1"
        break
    if re.search("AWS", cadena):
        continue
    else:
        break

print (cadena)

