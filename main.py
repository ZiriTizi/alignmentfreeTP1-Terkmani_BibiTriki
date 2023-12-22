from loading import load_directory
from kmers import stream_kmers, kmer2str
import time
import psutil
import heapq
import math
import numpy as np

start = time.time()
disk_before = psutil.disk_usage('/').used
distance = np.zeros((5,5))

def jaccard(s1, s2, k):
    j = 0
    taille_I , taille_U = 0,0
    dico = {}
    print('Start Jaccard')
    for kmer in s1:
        dico[kmer] = 1 if kmer not in dico else dico[kmer]+1
        taille_U += 1
    for kmer in s2:
        if kmer in dico:
            taille_I += 1
            if dico[kmer] != 0:
                dico[kmer] - 1   
            else :
                dico.pop(kmer)
        else :
            dico[kmer] = 1
            taille_U += 1

    j = taille_I/taille_U

    return j




def echantillon(file, k, s):
    h = [float('-inf')] * s  
    heapq.heapify(h)

    for kmer in stream_kmers(file, k):
        if -kmer > min(h):
            heapq.heappushpop(h, kmer) # the pop function pops the smallest value in the heap
    return h

if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("C:/Users/Lenovo/Downloads/TP2/alignmentfreeTP1-main/data")
    k = 32



    filenames = list(files.keys())
    print(filenames)
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            s1 = echantillon(files[filenames[i]][0],k,32)
            #print(s)
            s2 = echantillon(files[filenames[j]][0],k,32)
            jacc = jaccard(s1, s2, k)
            print(filenames[i], filenames[j], jacc)
            distance[i,j]=jacc
print(distance)


print('this actually took : ',time.time() - start)
disk_after= psutil.disk_usage('/').used
disk_used_by_program = disk_after-disk_before
print(f"Espace disque utilisé par le programme : {disk_used_by_program} octets")
