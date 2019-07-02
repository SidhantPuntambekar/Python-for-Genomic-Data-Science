#A program to find the canonical donor splice site candidates in an input DNA sequence

dna = input('Enter a DNA Sequence: ')
#A canonical donor splce site will always start with the base pair sequence GT
pos = dna.find('gt', 0)
while (pos>1) :
    print("Donor splice site at position %d"% pos)
    pos = dna.find('gt', pos+1)