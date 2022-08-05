# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)


def DNA_strand(dna):
    x = ''
    for i in dna:
        if i == 'A':
            x += 'T'
        elif i == 'C':
            x += 'G'
        elif i == 'T':
            x += 'A'
        elif i == 'G':
            x += 'C'
    return x



import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))


pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])


import string
TABLE = string.maketrans('ATCG', 'TAGC')
def DNA_strand(dna):
    return dna.translate(TABLE)

SYMBOLS = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

def DNA_strand(dna):
    complementary = ""
    
    for c in dna:
        symbol = SYMBOLS[c]
        complementary += symbol
    
    return complementary