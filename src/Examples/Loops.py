apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes:
    print(ape + " is an ape")

file = open("../../docs/4_dna_sequences.txt")
all_lines = file.readlines()
file.close()
print(all_lines)
for line in all_lines:
    line = line.replace("-", "")
    line = line.replace('"', '')
    sequences = line.split(" = ")
    print(str(sequences))
#    for nucleotides in sequences:

#    nucleotides = line[0]
#    nucleotides = nucleotides.upper()
#    print(str(nucleotides))
#    fasta = ">" + str(line)
#    print(str(fasta))
#    new_file = open("dna_sequences.fasta", "w")
#    new_file.write(fasta)
# open("dna_sequences.fasta")
