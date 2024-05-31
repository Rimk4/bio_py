NAMES: dict[str, str] = {
    "A": "Alanine",
    "R": "Arginine",
    "N": "Asparagine",
    "D": "Aspartic acid",
    "C": "Cysteine",
    "E": "Glutamic acid",
    "Q": "Glutamine",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "L": "Leucine",
    "K": "Lysine",
    "M": "Methionine",
    "F": "Phenylalanine",
    "P": "Proline",
    "S": "Serine",
    "T": "Threonine",
    "V": "Valine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
}

CODONS = {
    "A": (
        "GCA",
        "GCC",
        "GCG",
        "GCT",
    ),
    "C": (
        "TGC",
        "TGT",
    ),
    "D": (
        "GAC",
        "GAT",
    ),
    "E": (
        "GAA",
        "GAG",
    ),
    "F": (
        "TTC",
        "TTT",
    ),
    "G": (
        "GGA",
        "GGC",
        "GGG",
        "GGT",
    ),
    "H": (
        "CAC",
        "CAT",
    ),
    "I": (
        "ATA",
        "ATC",
        "ATT",
    ),
    "K": (
        "AAA",
        "AAG",
    ),
    "L": (
        "CTA",
        "CTC",
        "CTG",
        "CTT",
        "TTA",
        "TTG",
    ),
    "M": ("ATG",),
    "N": (
        "AAC",
        "AAT",
    ),
    "P": (
        "CCA",
        "CCC",
        "CCG",
        "CCT",
    ),
    "Q": (
        "CAA",
        "CAG",
    ),
    "R": (
        "AGA",
        "AGG",
        "CGA",
        "CGC",
        "CGG",
        "CGT",
    ),
    "S": (
        "AGC",
        "AGT",
        "TCA",
        "TCC",
        "TCG",
        "TCT",
    ),
    "T": (
        "ACA",
        "ACC",
        "ACG",
        "ACT",
    ),
    "V": (
        "GTA",
        "GTC",
        "GTG",
        "GTT",
    ),
    "W": ("TGG",),
    "Y": (
        "TAC",
        "TAT",
    ),
}

REVERSE_CODONS = dict((codon, aa) for aa, codons in CODONS.items() for codon in codons)

START_CODON = "ATG"
STOP_CODONS = (
    "TAA",
    "TAG",
    "TGA",
)

def read_rna(seq):
    result = ""
    for i in range(0, len(seq), 3):
        if seq[i:i+3] in STOP_CODONS:
            return result
        result += REVERSE_CODONS[seq[i:i+3]]

    return result


#print(read_rna(input()))
print(read_rna('CGUAUCGGUCACACCGCUAACAGCUGGGAAAGAUAG'.replace("U", "T")))