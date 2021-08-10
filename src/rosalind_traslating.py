'''
NAME
    rosalind_traslating.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa pide al usuario una secuencia de RNA mensajero y le da su equivalencia en aminoácidos.

CATEGORY
    Búsqueda de codones en secuencias

USAGE
    rosalind_traslating.py [sin argumentos]

ARGUMENTS
    No se requieren argumentos para este programa.

PACKAGES
    No se requiere algún paquete en específico para correr este programa.

FUNCTIONS
    No requeridas.

INPUT
    Secuencia de RNA perteneciente a un RNA mensajero.

OUTPUT
    Secuencia de aminoácidos tras la traducción del RNA.

EXAMPLES
    Se tiene la secuencia AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA. Esta secuencia es escrita por el usuario
    tras ver el mensaje que la solicita. Después, el programa reemplaza las bases U por T (dado que el código de
    aminoácidos en el diccionario está escrito para ADN), y después divide la secuencia en tripletes para poder buscar
    así su traducción. Al final, se va recorriendo la lista de codones y se va buscando cada uno de ellos en el
    diccionario, imprimiendo después su respectivo aminoácido. Así, tenemos que la secuencia de aminoácidos sería:
    MAMAPRTEINSTRING_
    Nota: el output imprime cada aminoácido con un salto de línea.

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/rosalind_traslating.py

'''

# 1. Pedir secuencia de RNA.
print("Escriba una secuencia de mRNA: ")
s = input()

# 2. Reemplazar uracilos por timinas.
dna = s.replace('U', 'T')

# 3. Dividir secuencia en tripletes.
division = [dna[i:i+3] for i in range(0, len(dna), 3)]

# 4. Definir diccionario con código de aminoácidos.
gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

# 5. Buscar cada codón en el diccionario e imprimir su traducción a aminoácido.
print("La secuencia de RNA traducida a aminoácidos es: ")
for codon in division:
    print(gencode[codon])
