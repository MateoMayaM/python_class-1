# Este programa saca la cadena que seria complementaria a la de ADN mostrada en el input (es decir, la de mRNA)

print("Escriba la secuencia de DNA (la hebra codificante): ")
sequence_input = input()


def dna_conversion(sequence):
    # Se revierte la secuencia dada por el usuario
    dna = sequence[::-1]
    dna = dna.replace("A", "t")
    dna = dna.replace("C", "g")
    dna = dna.replace("G", "c")
    dna = dna.replace("T", "a")
    print(f"Secuencia de RNA complementaria a la de DNA escrita (hebra no codificante, escrita de 5' a 3'): "
          f"{dna.upper()}")
    rna = sequence.replace("T", "U")
    print(f'Secuencia de mRNA perteneciente a la de ADN: {rna}')


dna_conversion(sequence_input)
