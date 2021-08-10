# Este programa lee un archivo con un máximo de 1000 líneas y regresa un archivo con las lineas pares del anterior.

# 1. Leer el archivo
f = open('rosalind_ini5.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
    line.split("\n")

division = lines[1::2]
output = open('output.txt', 'w')
for div in division:
    output.write(str(div))
