""" A program to compute the gc percentage of a given DNA sequence 
"""

# get DNA sequence:
dna = input("Enter a DNA sequence, please: ")
no_a = dna.count('a')
no_c = dna.count('c')
no_g = dna.count('g')
no_t = dna.count('t')
dna_length = len(dna)
gc_percentage = (no_c+no_g)*100.0/dna_length
at_percentage = (no_a+no_t)*100.0/dna_length
printStringAT = "The A-T percentage of this DNA sequence is: "
printStringGC = "The G-C percentage of this DNA sequence is: "
print(printStringAT + str(at_percentage))
print(printStringGC + str(gc_percentage))