'''
NAME
    transcription.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este módulo calcula lo que sería la secuencia de mRNA al transcribir una cadena de ADN.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    Ejecutar archivo modulos_final.py (en ese archivo se incluye la paquetería que contiene a transcription.py):
        modulos_final.py [sin argumentos]

ARGUMENTS
    No requeridos

PACKAGES
    proyecto_final          Este paquete contiene a los módulos requeridos que trabajan con una secuencia de DNA.

FUNCTIONS
    dna_to_rna          Convierte la cadena de DNA dada en RNA.

INPUT
     Secuencia de ADN.

OUTPUT
    Secuencia de ARN (en el caso de transcription.py):
        Secuencia de RNA perteneciente a la de DNA: <cadena de RNA>

EXAMPLES
    Example 1: Se tiene la secuencia ATGGCGCCGTGA. Esta secuencia entra a la función dna_to_rna disponible en el módulo,
    donde se reemplaza a las bases timina (T) por uracilo (U). Al final, se imprime la cadena resultante. Así, tenemos:
        Secuencia de RNA perteneciente a la de DNA: AUGGCGCCGUGA

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/proyecto_final/transcription.py
    Ejecución: https://github.com/Danigore25/python_class/blob/master/src/modulos_final.py

'''

# Definir función.


def dna_to_rna(sequence):
    """
    La función dna_to_rna convierte la secuencia de DNA en RNA convirtiendo las bases timina en uracilos.
    :param sequence: Secuencia de DNA dada por el usuario.
    :return: Secuencia de RNA que pertenecería a la generada en el input.
    """
    # 1. Convertir bases timinas a uracilos.
    rna = sequence.replace("T", "U")

    # 2. Imprimir secuencia de RNA.
    print(f'Secuencia de RNA perteneciente a la de DNA: {rna}')
