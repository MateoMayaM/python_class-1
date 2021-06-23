'''
NAME
    modulo2.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este módulo imprime la cadena complementaria a una secuencia de DNA dada por el usuario.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    Ejecutar archivo modulos_final.py (en ese archivo se incluye la paquetería que contiene a modulo2.py):
        modulos_final.py [sin argumentos]

ARGUMENTS
    No requeridos

PACKAGES
    proyecto_final          Este paquete contiene a los módulos requeridos que trabajan con una secuencia de DNA.

FUNCTIONS
    dna_reverse             Regresa la cadena que sería complementaria a la secuencia dada en el input.

INPUT
     Secuencia de ADN.

OUTPUT
    Cadena complementaria (en el caso de modulo2.py):
        Secuencia de RNA complementaria a la de DNA escrita (hebra no codificante, escrita de 5' a 3'): <cadena>

EXAMPLES
    Example 1: Se tiene la secuencia ATGGCGCCGTGA, la cual es escrita por el usuario a través del archivo
    modulos_final.py. La secuencia entra a la función dna_reverse, donde se revierte la cadena (para obtener la
    cadena complementaria escrita de 5' a 3'), se reemplaza cada una de las bases por su contraparte (A por T y
    viceversa, y G por C y al revés) poniendo cada base reemplazada en minúsculas (esto se realiza para no confundir las
    bases cambiadas recientemente con las originales). Al final, se imprime la cadena resultante al convertirla en una
    con letras mayúsculas. De esta forma, queda que:
        Secuencia de RNA complementaria a la de DNA escrita (hebra no codificante, escrita de 5' a 3'): TCACGGCGCCAT

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/proyecto_final/modulo2.py
    Ejecución: https://github.com/Danigore25/python_class/blob/master/src/modulos_final.py

'''

# Definir función.


def dna_reverse(sequence):
    """
    La función dna_conversion calcula la cadena complementaria a la dada por el usuario, regresando la secuencia
    resultante con una orientación de 5' a 3'.
    :param sequence: Secuencia input dada por el usuario.
    :return: Secuencia complementaria a la escrita, de 5' a 3'.
    """
    # 1. Revertir la secuencia dada por el usuario.
    dna = sequence[::-1]

    # 2. Reemplazar bases de la secuencia por las complementarias correspondientes.
    dna = dna.replace("A", "t")
    dna = dna.replace("C", "g")
    dna = dna.replace("G", "c")
    dna = dna.replace("T", "a")

    # 3. Imprimir la cadena complementaria, convirtiendo a mayúsculas las bases.
    print(f"Secuencia de RNA complementaria a la de DNA escrita (hebra no codificante, escrita de 5\' a 3\'): "
          f"{dna.upper()}")
