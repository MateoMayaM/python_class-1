import re


class AmbiguousBaseError (Exception):
    pass


def contenido_at(dna):
    try:
        if re.finditer(r"[^ATCG]", dna):
            raise AmbiguousBaseError

        elif re.finditer(r"[ATCG]", dna):
            alto_at = re.finditer(r"[AT]{5,}", dna)
            if alto_at and re.finditer(r"[ATCG]", dna):
                for at in alto_at:
                    region = at.group()
                    start = at.start()
                    final = at.end()
                    print("Región rica en contenido de AT: (", start, ",", final, "), match: ", region)
        elif re.finditer(r"[ATCG]", dna) and not re.search(r"[AT]{5,}", dna):
            print("No se encontraron regiones ricas en AT")

    except AmbiguousBaseError:
        matches = re.finditer(r"[^ATCG]", dna)
        if not matches:
            print("Se encontró uno o más caracteres no pertenecientes a bases nucleotídicas: ")
        for m in matches:
            base = m.group()
            pos = m.start()
            print(base, " encontrada en posición ", str(pos))

print("Escriba la secuencia de DNA: \n")
dna_input = input()
contenido_at(dna_input)
