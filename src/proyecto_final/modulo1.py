'''
NAME
    modulo1.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este módulo calcula el contenido de GC de una secuencia de DNA.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    Ejecutar archivo modulos_final.py (en ese archivo se incluye la paquetería que contiene a modulo1.py):
        modulos_final.py [sin argumentos]

ARGUMENTS
    No requeridos

PACKAGES
    proyecto_final          Este paquete contiene a los módulos requeridos que trabajan con una secuencia de DNA.

FUNCTIONS
    get_gc_content          Calcula el contenido de las bases G y C juntas de una secuencia de DNA.

INPUT
     Secuencia de ADN.

OUTPUT
    Contenido de GC de la secuencia (en el caso de modulo1.py):
        El porcentaje de GC en la secuencia es:  <contenido de GC calculado> %

EXAMPLES
    Example 1: Se tiene la secuencia ATGGCGCCGTGA, ésta es escrita como input y entra a la función get_gc_content.
    Dentro de la misma se saca su longitud, se cuenta la cantidad de bases G y C y se calcula el contenido que tiene de
    ambas, sumándolas y dividiéndolas entre la longitud (y multiplicándolas por cien para sacar el porcentaje). Al
    final, se imprime el resultado redondeando la cantidad a dos decimales para que sea más fácil interpretarlo. De esta
    manera, se obtiene:
        El porcentaje de GC en la secuencia es:  66.67 %

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/proyecto_final/modulo1.py
    Ejecución: https://github.com/Danigore25/python_class/blob/master/src/modulos_final.py

'''

# Definir función.


def get_gc_content(sequence):
    """
    La función calcula el contenido de GC de una secuencia de DNA, sumando la cantidad de ambas bases y dividiéndola
    entre la longitud que contiene la cadena.
    :param sequence: Secuencia input de DNA dada por el usuario.
    :return: Contenido de GC de la secuencia de DNA redondeada con dos decimales.
    """
    # 1. Calcular la longitud de la secuencia.
    length = len(sequence)

    # 2. Contar las bases por separado.
    g_count = sequence.count('G')
    c_count = sequence.count('C')

    # 3. Calcular el contenido de ambas bases por cada cien.
    gc_content = ((g_count + c_count) / length) * 100

    # 4. Imprimir resultado redondeado con dos decimales.
    print('El porcentaje de GC en la secuencia es: ', round(gc_content, 2), '%')
