from __future__ import annotations
import itertools

class SequenceGenerator:
    aminoacidTable = {
        'A': [ 'GCT', 'GCC', 'GCA', 'GCG' ],
        'R': [ 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG' ],
        'N': [ 'AAT', 'AAC' ],
        'D': [ 'GAT', 'GAC' ],
        'C': [ 'TGT', 'TGC' ],
        'Q': [ 'CAA', 'CAG' ],
        'E': [ 'GAA', 'GAG' ],
        'G': [ 'GGT', 'GGC', 'GGA', 'GGG' ],
        'H': [ 'CAT', 'CAC' ],
        'I': [ 'ATT', 'ATC', 'ATA' ],
        'L': [ 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG' ],
        'K': [ 'AAA', 'AAG' ],
        'M': [ 'ATG' ],
        'F': [ 'TTT', 'TTC' ],
        'P': [ 'CCT', 'CCC', 'CCA', 'CCG' ],
        'S': [ 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC' ],
        'T': [ 'ACT', 'ACC', 'ACA', 'ACG' ],
        'W': [ 'TGG' ],
        'Y': [ 'TAT', 'TAC' ],
        'V': [ 'GTT', 'GTC', 'GTA', 'GTG' ]
    }
    stopTranslationCodons = [ 'TAA', 'TAG', 'TGA' ]
    
    def __init__(self, peptide: str = "") -> None:
        if not self.validate_sequence(peptide):
            raise Exception("Invalid sequence")

        self.codonSetsSequences = [ self.aminoacidTable[aminoacid] for aminoacid in peptide ]
        self.codonSetsSequences.append(self.stopTranslationCodons)

        self.dnaSequences = itertools.product(*self.codonSetsSequences)

        self.currentSequence = 0
        self.possibleSequencesNumber = self.possible_sequences_number()

    def __iter__(self) -> SequenceGenerator:
        return self

    def __next__(self) -> None:
        return self.next()

    def next(self) -> str:
        if self.currentSequence == self.possibleSequencesNumber:
            raise StopIteration
        self.currentSequence += 1
        return next(self.dnaSequences)

    def possible_sequences_number(self) -> int:
        n = 1
        for codonList in self.codonSetsSequences:
            n *= len(codonList)
        return n

    def validate_sequence(self, peptide: str) -> bool:
        for aminoacid in peptide:
            if not aminoacid in self.aminoacidTable.keys():
                return False
        return True
