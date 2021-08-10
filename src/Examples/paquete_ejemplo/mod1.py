import re

def fun1(cadena):
    matches = re.finditer(r"[n]", cadena)
    if matches:
        for m in matches:
            base = m.group()
            pos = m.start()
            print(base + " encontrada en la posición " + str(pos))
    else:
        print("La cadena que usted escribió es ", cadena)
