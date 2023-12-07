def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text, k):
    #print('Begin stream kmer')
    encodage ={'A':0 ,'C':1,'T':2, 'G':3}
    mask = (1 << (k*2)) - 1
    x = 0
    rx = 0
    i = 0
    for letter in text:
        y = encodage[letter] 
        x <<= 2
        x += y
        x &= mask
        i +=1
        
        rx >>= 2
        complement = (y + 2) & 0b11
        rx += complement << (k-1)*2

        if(i > k - 1):
            yield(min(x,rx))




