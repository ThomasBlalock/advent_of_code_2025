#%%
with open('data/day5.txt', 'r') as file:
    data = file.read()
data = data.split('\n\n')
fresh = data[0].split('\n')
fresh = [f.split('-') for f in fresh]
available = data[1].split('\n')


# Puzzle 1
ttl = 0
for a in available:
    for f in fresh:
        if int(a) >= int(f[0]) and int(a) <= int(f[1]):
            ttl += 1
            break
print(ttl)


# Puzzle 2
fresh = [(int(f[0]), int(f[1])) for f in fresh]
fresh.sort()

mmap = [True]*len(fresh)
i = 0
while i < len(fresh)-1:
    if fresh[i][1] >= fresh[i+1][0]:
        fresh[i+1] = (fresh[i][0], max(fresh[i][1], fresh[i+1][1]))
        mmap[i] = False
    else:
        mmap[i] = True
    i += 1

fresh_fixed = []
for i in range(len(fresh)):
    if mmap[i]:
        fresh_fixed.append(fresh[i])

ttl = sum([f[1]-f[0]+1 for f in fresh_fixed])
print(ttl) # 345039628276631 > x