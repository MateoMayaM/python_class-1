# Este programa toma en cuenta dos variables e imprime el resultado de la suma de los número contenidos entre esas
# cantidades.

print("Escriba el valor número 1: ")
a = input()
print("Escriba el valor número 2: ")
b = input()
if (a < b) < 10000:
    suma = 0
    for i in range(int(a), int(b)):
        if i % 2 == 1:
            suma = suma + i
    print(suma)
