

dna_string = input().lower()
guanin = dna_string.count('g')
citosin = dna_string.count('c')
result = guanin + citosin
percent_s = (result / len(dna_string)) * 100
print(percent_s)
