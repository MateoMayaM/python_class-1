file = open("rosalind_text")
all_lines = file.readlines()
cadena = 0
for line in all_lines:
    n = line.replace("\n", "")
    cadena = str(cadena) + str(n)

print(cadena)

file.close()
