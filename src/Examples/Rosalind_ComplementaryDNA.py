print("DNA sequence: ")
sequence = input()
dna = sequence[::-1]     # Se revierte la secuencia dada por el usuario
dna = dna.replace("A", "t")
dna = dna.replace("C", "g")
dna = dna.replace("G", "c")
dna = dna.replace("T", "a")
print(f"Complementary DNA: {dna.upper()}")
