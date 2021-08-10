import re

# a = 'CGT'
# b = 'ATG'
# dna = 'ATGACGTACGT'
# if re.search(b, dna) or re.search(a, dna):
#    print('found!')


# class AmbiguousBaseError (Exception):
#    pass


# if re.search(r"[^ATCG]", dna):
#    raise AmbiguousBaseError('ambiguous base error!')

# dna = 'ATCGCGAATTCACGGnCC'

'''
def check_bases(adn):
    if not re.search(r"[ATCG]", adn):
        raise ValueError('no bases found!')
    m = re.search(r"[^ATCG]", adn)
    if m:
        amb_base = m.group()
        raise ValueError(f'ambiguous base found: {amb_base}')
    return


check_bases(dna)
'''

'''
scientific_name = "Homo sapiens"
m = re.search(r"(.+) (.+)", scientific_name)
if m:
    genus = m.group(1)
    species = m.group(2)
    print("genus is " + genus + ", species is " + species)
'''

'''
dna = "CGATnCGAACGATC" 
m = re.search(r"[^ATGC]", dna) 
if m: 
    print("ambiguous base found!") 
    print("at position " + str(m.start()))
'''


dna = "CGCTCnTAGATGCGCrATGACTGCAyTGC" 
matches = re.finditer(r"[^ATGC]", dna)
for m in matches: 
    base = m.group() 
    pos = m.start()
    print(base + " found at position " + str(pos))



