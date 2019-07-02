#A program to find the canonical donor splice site candidates in an input DNA sequence

dna = input('Enter a DNA Sequence: ')
#A canonical donor splce site will always start with the base pair sequence GT
pos = dna.find('gt', 0)