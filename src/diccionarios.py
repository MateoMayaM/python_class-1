# Variables
dna = "AATGATGAACGAC"
bases = ['A', 'T', 'G', 'C']
all_counts = {}
# Creating dinucleotides and counting
for base1 in bases:
    for base2 in bases:
        dinucleotide = base1 + base2
        count = dna.count(dinucleotide)
        if count > 0:
            all_counts[dinucleotide] = count

for key, value in all_counts.items():
    if value == 2:
        print(key)
