dna = input("Enter a DNA sequence:")
def has_stop_codon(dna,frame) :
    "This function checks if dna sequence has an in frame stop codon"
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame,len(dna),3) :
        codon = dna[i:i+3].lower()
        if codon in stop_codons :
            stop_codon_found = True
            break
    return stop_codon_found

if(has_stop_codon(dna))
    print("Input sequence has a stop codon")
else:
    print("Input sequence does not have a stop codon")