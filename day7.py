#%%
with open('data/day7.txt', 'r') as file:
    data = file.read()
data = data.split('\n')

# Puzzle 1
ttl = 0
beam_idxs = set()
for line in data:
    for i, c in enumerate(line):
        if c == 'S':
            beam_idxs.add(i)
        if c == '^' and i in beam_idxs:
            ttl += 1
            beam_idxs.remove(i)
            beam_idxs.add(i-1)
            beam_idxs.add(i+1)
print(ttl)

# Puzzle 2
beams = [0]*len(data[0])
for line in data:
    for i, c in enumerate(line):
        if c == 'S':
            beams[i] += 1
        if c == '^':
            beams[i-1] += beams[i]
            beams[i+1] += beams[i]
            beams[i] = 0
ttl = sum(beams)
print(ttl)