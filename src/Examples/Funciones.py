def get_at_content(dna):
    dna = dna.replace('N', '')
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count)/length
    return round(at_content, 2)


print("Write a dna sequence: ")
dna_input = input()
print("AT content is " + str(get_at_content(dna_input)))


def get_content_amino_acid(protein, amino_acid):
    protein = protein.upper()
    length = len(protein)
    amino_acid = amino_acid.upper()
    amino_acid_count = protein.count(amino_acid)
    amino_content = (amino_acid_count/length)*100
    return round(amino_content, 2)


print("Write a protein sequence: ")
protein_input = input()
print("Write an amino acid: ")
amino_acid_input = input()
print("The content of the amino acid " + str(amino_acid_input) + " in the protein sequence is " +
      str(get_content_amino_acid(protein_input, amino_acid_input)) + "%")
