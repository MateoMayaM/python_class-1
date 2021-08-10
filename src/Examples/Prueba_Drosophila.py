file = open("../../docs/6-data.csv")
lines = file.readlines()
file.close()


def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('a')
    t_count = dna.count('t')
    at_content = (a_count + t_count)/length
    return at_content


for line in lines:
    sequences = line.split(",")
#    print(sequences[1])

#    if sequences[0] == 'Drosophila melanogaster' or sequences[0] == 'Drosophila simulans':
#        print("Gen perteneciente a " + str(sequences[0]) + ": " + str(sequences[2]))

#    if (len(sequences[1]) > 90) and (len(sequences[1]) < 110):
#        print("El gen " + str(sequences[2]) + " tiene " + str(len(sequences[1])) + " bases de longitud")

#    print(str(get_at_content(sequences[1])) + " " + str(sequences[2]))


#    if (get_at_content(sequences[1]) < 0.5) and (int(sequences[3]) > 200):
#        print("El gen " + str(sequences[2]) + " tiene un contenido de AT menor que 0.5 y un nivel de expresión mayor "
#                                              "que 200")

#   if (sequences[2].startswith('k') or sequences[2].startswith('h')) and not sequences[0] == 'Drosophila melanogaster':
#        print("El gen " + str(sequences[2]) + " comienza con k o con h y no pertenece a Drosophila melanogaster")

#    if get_at_content(sequences[1]) > 0.65:
#        print("El gen " + str(sequences[2]) + " tiene un contenido de AT alto")
#    elif get_at_content(sequences[1]) < 0.45:
#        print("El gen " + str(sequences[2]) + " tiene un contenido de AT bajo")
#    else:
#        print("El gen " + str(sequences[2]) + " tiene un contenido de AT medio")
