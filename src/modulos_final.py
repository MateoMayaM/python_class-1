'''
NAME
    modulos_final.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa pide una secuencia de DNA al usuario y la evalúa en funciones descritas en módulos de una paquetería.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    Ejecutar archivo modulos_final.py (en ese archivo se invoca a la paquetería con todos los módulos):
        modulos_final.py [sin argumentos]

ARGUMENTS
    No requeridos

PACKAGES
    proyecto_final          Este paquete contiene a los módulos requeridos que trabajan con una secuencia de DNA.

FUNCTIONS
    get_gc_content          Calcula el contenido de las bases G y C juntas de una secuencia de DNA.
    dna_reverse             Regresa la cadena que sería complementaria a la secuencia dada en el input.
    dna_to_rna              Convierte la cadena de DNA dada en RNA.
    translating             Traduce la secuencia de DNA dada por el usuario a sus aminoácidos correspondientes.

INPUT
     Secuencia de ADN.

OUTPUT
    Resultados al llamar las funciones de los módulos:
        El porcentaje de GC en la secuencia es:  <contenido de GC calculado> %
        Secuencia de RNA complementaria a la de DNA escrita (hebra no codificante, escrita de 5' a 3'): <cadena>
        Secuencia de mRNA perteneciente a la de ADN: <cadena de RNA>
        La secuencia de DNA traducida a aminoácidos es: <secuencia de aminoácidos>

EXAMPLES
    Example 1: Se tiene la secuencia ATGGCGCCGTGA, la cual es escrita por el usuario como input. El programa llama
    anteriormente a la paquetería para después invocar a las funciones dentro del mismo (no es necesario mencionar
    directamente a cada uno de los módulos en el programa puesto que eso está escrito en el programa __init__.py).
    Dentro de cada función se realiza una actividad distinta: get_gc_content calcula el contenido de GC de la secuencia,
    dna_reverse muestra lo que sería la cadena complementaria a la dada por el usuario escrita de 5' a 3', dna_to_rna
    indica cómo sería la cadena de mRNA si la de ADN se transcribiera y translating muestra la secuencia de aminoácidos
    que se tendría al traducir el DNA.
    En este ejemplo en específico se tendrían los siguientes resultados:
        El porcentaje de GC en la secuencia es:  66.67 %
        Secuencia de RNA complementaria a la de DNA escrita (hebra no codificante, escrita de 5' a 3'): TCACGGCGCCAT
        Secuencia de mRNA perteneciente a la de ADN: AUGGCGCCGUGA
        La secuencia de DNA traducida a aminoácidos es:
        MAP

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/modulos_final.py

'''

# 1. Importar paquete.
import proyecto_final

# 2. Pedir secuencia al usuario.
print('Escriba la secuencia de DNA (la hebra codificante escrita de 5\' a 3\')')
sequence_input = input()

# 3. Llamar a las funciones incluídas dentro de los módulos del paquete.
# proyecto_final.get_gc_content(sequence_input)
# proyecto_final.dna_reverse(sequence_input)
# proyecto_final.dna_to_rna(sequence_input)
proyecto_final.translating(sequence_input)
