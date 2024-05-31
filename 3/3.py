from functools import reduce


def is_tranzition(c1, c2):
    return (c1 + c2).upper() in ("AG", "CT", "GA", "TC")

def is_transversion(c1, c2):
    return c1 != c2 and not is_tranzition(c1, c2)

def get_ratio(s1, s2):
    merged = [(s1[i], s2[i]) for i in range(len(s1))]
    count_tranzitions = reduce(lambda count, next: count + int(is_tranzition(next[0], next[1])), merged, 0)
    count_transvers = reduce(lambda count, next: count + int(is_transversion(next[0], next[1])), merged, 0)

    return (count_tranzitions / count_transvers)

#s1 = input()
#s2 = input()

s1 = 'ACGATCGCATGTCATCAACGTTTACGGCATGCAGCTAGCGATCGATTTCGCTATGCTTAGCATGACTCGGACTACGACTACGACT'
s2 = 'GCTAGTCACCACAGTCGCGATCGACGATCGGATCTCGACTTCGACTACTAGCGCGATTCGAAATCAGCTCGACTATTCGGGTATC'

print(get_ratio(s1, s2))