'''
NAME
    Busqueda_codon_secuencia.py

VERSION
    2.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa busca el codón de inicio TAC en una secuencia de ADN y ve hasta dónde abarca, tomando en cuenta el
    codón de paro ATT. Después, imprime la secuencia de ADN que se transcribe.

CATEGORY
    Búsqueda de codones en secuencias

USAGE
    Busqueda_codon_secuencia.py [sin opciones]

ARGUMENTS
    [sin argumentos]

INPUT
    dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'

OUTPUT
    El codón de inicio TAC se encuentra en la posición  4 y termina en  19
    Fragmento de DNA que será transcrito:  TACGTCGCGCGTT


EXAMPLES
    Example 1: Se tiene la secuencia AAGGTACGTCGCGCGTTATTAGCCTAAT (que representa el input del programa), la cual es
    anotada en la variable adn escrita por el programador. Después se guarda el codón TAC en la variable inicio, y el
    codón de paro ATT en la variable paro. Luego se imprime la posición donde se ubica el codón de inicio hasta donde
    se ubica el codón de paro más dos (se suma dos dado que la posición del codón es la ubicación de su primer
    nucleótido, mientras que dos nucleótidos más adelante es el sitio donde termina el codón de paro). Por último, se
    imprime el fragmento de ADN que será escrito mediante un corte con las variables inicio y paro
    (adn[(adn.find(inicio)):(adn.find(paro))]))).

GITHUB LINK
    Liga de GitHub donde se encuentra el programa:
    https://github.com/Danigore25/python_class/blob/master/src/Busqueda_codon_secuencia.py

'''

adn = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'   # Aquí se muestra la secuencia de ADN donde queremos buscar los codones.
inicio = 'TAC'   # Este es el codón de inicio de la secuencia (AUG -> TAC).
paro = 'ATT'   # Este es el codón de paro de la secuencia (UAA -> ATT).
print("El codón de inicio TAC se encuentra en la posición ", adn.find(inicio), "y termina en ", adn.find(paro)+2)
# Aquí se busca la posición en donde se encuentra el codón de inicio, mientras que para ver dónde termina se le suma un
# dos a la posición del codón de paro dado que termina dos bases después de donde empieza (es un triplete).

print("Fragmento de DNA que será transcrito: ", adn[(adn.find(inicio)):(adn.find(paro))])
# Aquí se menciona las bases que conforman el fragmento desde el codón de inicio hasta antes del codón de paro.
