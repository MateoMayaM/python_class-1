'''
NAME
    modulo4.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este módulo pide al usuario una secuencia de DNA y le da su equivalencia en aminoácidos.

CATEGORY
    Búsqueda de codones en secuencias

USAGE
    Ejecutar archivo modulos_final.py (en ese archivo se incluye la paquetería que contiene a modulo4.py):
        modulos_final.py [sin argumentos]

ARGUMENTS
    No requeridos

PACKAGES
    proyecto_final          Este paquete contiene a los módulos requeridos que trabajan con una secuencia de DNA.

FUNCTIONS
    translating          Traduce la secuencia de DNA dada por el usuario a sus aminoácidos correspondientes.

INPUT
     Secuencia de ADN.

OUTPUT
    Secuencia de aminoácidos (en el caso de modulo4.py):
        La secuencia de DNA traducida a aminoácidos es: <secuencia de aminoácidos>

EXAMPLES
    Example 1: Se tiene la secuencia ATGGCGCCGTGA, la cual contiene cuatro codones. La secuencia es escrita por el
    usuario y entra a la función translating, donde se divide por tripletes (para así irlos traduciendo). Después, se
    crea una lista donde se irá guardando la traducción de cada codón, esto siendo guiado gracias a un diccionario
    presente en el módulo que contiene la equivalencia de cada terna de bases en aminoácidos. Por último, se imprime la
    secuencia de aminoácidos resultante de forma continua. En este ejemplo, tenemos como resultado:
        La secuencia de DNA traducida a aminoácidos es:
        MAP
    NOTA: No aparece la equivalencia del último codón dado que éste marca un paro en la secuencia de aminoácidos.

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/proyecto_final/modulo4.py
    Ejecución: https://github.com/Danigore25/python_class/blob/master/src/modulos_final.py

'''

# 1. Definir diccionario con código de aminoácidos.
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
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
    'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W'}


# 2. Definir función.
def translating(sequence):
    """
    Esta función convierte la secuencia de DNA dada a aminoácidos utilizando un diccionario que contiene la traducción
    de los codones.
    :param sequence: Secuencia de DNA escrita por el usuario.
    :return: Secuencia de aminoácidos equivalente a la secuencia input.
    """
    # 3. Dividir secuencia en tripletes.
    division = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

    # 4. Buscar cada codón en el diccionario, guardar su traducción a aminoácido en una lista.
    print("La secuencia de DNA traducida a aminoácidos es: ")
    protein = []
    for codon in division:
        protein.append(gencode[codon])

    # 5. Imprimir lista con aminoácidos.
    print(*protein, sep='')
