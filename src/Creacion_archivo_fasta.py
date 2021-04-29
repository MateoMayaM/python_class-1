# PONER ENCABEZADO

# 1. Se abre el archivo 4_dna_sequences.txt que se encuentra en la carpeta docs de python_class (con el directorio
# "../docs/4_dna_sequence.txt").
file = open("../docs/4_dna_sequences.txt")

# 2. Se leen las líneas contenidas en el archivo, y se guardan en la variable all_lines.
all_lines = file.readlines()

# 3. Se cierra el archivo 4_dna_sequences.txt que se había guardado en la variable file.
file.close()

# 4. Se abre un archivo nuevo (en este caso se llamará dna_sequences.fasta).
#    new_file = open("dna_sequences.fasta", "w")

# 5. Se realiza un for que irá recorriendo las líneas contenidas en el archivo anterior.
for line in all_lines:
    line = line.replace("-", "")    # Esta línea reemplaza los guiones de una de las secuencias por nada.
    line = line.replace('"', '')     # Esta línea reemplaza las comillas por nada.
    line = line.replace("\n", "")    # Esta línea cambia los saltos de línea por nada (se pondrán más tarde).
    sequences = line.split(" = ")    # Esta línea divide la cadena de cada secuencia en dos partes gracias al split.
    name = sequences[0]    # Esta línea guarda la cadena de cada secuencia que contiene el nombre de la misma.
    nucleotides = sequences[1:32]    # Esta línea guarda la cadena de la secuencia que contiene los nucleótidos.
# son hasta 32 porque es el máximo número de nucleótidos que tenemos en la secuencias.

    bases = str(nucleotides).upper()    # Aquí se convierte la secuencia de nucleótidos a mayúsculas y se guarda.

#    fasta = ">" + str(line)
#    print(str(fasta))
#    new_file.write(fasta)

# 6. Se cierra el archivo nuevo (en este caso, se encuentra escrito en new_file).
