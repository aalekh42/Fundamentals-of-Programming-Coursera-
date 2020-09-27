def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    >>> get_length('')
    0
    """
    count=0
    for char in dna:
        count+=1
    return count

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if get_length(dna1) > get_length(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count=0
    for char in dna:
        if nucleotide == char:
            count+=1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    """
    (str) -> bool

    Return True if dna has no characters other than 'A','C','T','G' else False
    
    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('ADER')
    False
    >>>is_valid_sequence('ader')
    False
    >>>is_valid_sequence('AWQR')
    False
    >>>is_valid_sequence('A')
    True
    
    """
    count=0
    for char in dna:
        if char not in 'ATCG':
            count+=1

    if count > 0:
        return False
    else:
        return True

def insert_sequence(dna1,dna2,index):
    """
    (str,str,int) -> str

    Return dna sequence obtained by inserting dna2 sequence into the dna1
    sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    CCATGG
    >>>insert_sequence('CGTA','ATT',0)
    ATTCGTA
    >>>insert_sequence('CCTTC','AT',4)
    CCTTATC
    
    """
    dna=dna1[0:index]+dna2+dna1[index:len(dna1)]
    return dna

def get_complement(nucleotide):
    """

    (str) -> str
    
    Return Complement of Nucleotide.Nucleotide A's Complement is T and Vice versa
    similarly for C it's G.
    
    >>>get_complement('A')
    T
    >>>get_complement('G')
    C
    
    """

    if nucleotide =='A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide =='C':
        return 'G'
    else:
        return 'C'

def get_complementary_sequence(dna):
    """
    (str) -> str

    Return Dna sequence which is complemtary to the given sequence.
    
    >>>get_complementary_sequence('AT')
    TA
    >>>get_complementary_sequence('AGCC')
    TCGG
    """
    dna_new=''
    for char in dna:
        dna_new=dna_new+get_complement(char)
    return dna_new
