def gc(dna) :
#This function computes the gc percentage of DNA
    numbases = dna.count('n')+dna.count('N')
    gcPercent = float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G')*100/len(dna)-numbases)
    return gcPercent
print(gc('AAAGTNNAGTCC'))
    