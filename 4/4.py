def get_positions(s, t):
    inds = set()
    for i in range(len(s)):
        if s.find(t, i) == -1:
            return inds
        inds.add(s.find(t, i))

s = 'AGCGCGCATATGCGCGAAT'
t = 'GCGC'

print(*sorted(list(get_positions(s, t))))