def proteins(strand):
    codon_acid_mapping = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
    }
    codons = []
    for i in range(0, len(strand), 3):
        codons.append(strand[i:i+3])
    acids = []
    for codon in codons:
        if codon in ["UAA", "UAG", "UGA"]:
            return acids
        for key, value in codon_acid_mapping.items():
            if codon in value:
                acids.append(key)
    return acids
