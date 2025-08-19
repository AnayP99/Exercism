def to_rna(dna_strand):
    dna_ran_dict = {"A":"U", "G":"C", "C":"G", "T":"A"}
    result = ""
    for char in dna_strand:
        result += dna_ran_dict[char]
    return result
