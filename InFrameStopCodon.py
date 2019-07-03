dna = input("Enter a DNA sequence:")
def has_stop_codon(dna) :
    "This function checks if dna sequence has an in frame stop codon"
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(0,len(dna),3) :
        codon = dna[i:i+3].lower()

if(has_stop_codon(dna))
    print("Input sequence has a stop codon")
else:
    print("Input sequence does not have a stop codon")