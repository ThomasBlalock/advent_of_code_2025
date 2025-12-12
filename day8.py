#%%
with open('data/day8.txt', 'r') as file:
    data = file.read()
data = data.split('\n')
import heapq

# Puzzle 1
heap = []
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        line1 = data[i].split(',')
        line2 = data[j].split(',')
        x1, y1, z1 = int(line1[0]), int(line1[1]), int(line1[2])
        x2, y2, z2 = int(line2[0]), int(line2[1]), int(line2[2])
        dist = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5
        t = (dist, i, j)
        heapq.heappush(heap, t)

clusters = [i for i in range(len(data))]
for _ in range(1000):
    dist, i, j = heapq.heappop(heap)
    ci = clusters[i]
    cj = clusters[j]
    if ci == cj:
        continue
    c = min(ci, cj)
    for k in range(len(clusters)):
        if clusters[k] == ci or clusters[k] == cj:
            clusters[k] = c

cluster_sizes = {}
for i in range(len(clusters)):
    c = clusters[i]
    if c not in cluster_sizes:
        cluster_sizes[c] = 0
    cluster_sizes[c] += 1

cluster_sizes = sorted(cluster_sizes.items(), key=lambda x: x[1], reverse=True)
print(cluster_sizes[0][1]*cluster_sizes[1][1]*cluster_sizes[2][1])


# Puzzle 2
while sum(clusters) > 0:
    dist, i, j = heapq.heappop(heap)
    ci = clusters[i]
    cj = clusters[j]
    if ci == cj:
        continue
    c = min(ci, cj)
    for k in range(len(clusters)):
        if clusters[k] == ci or clusters[k] == cj:
            clusters[k] = c

print(int(data[i].split(',')[0]) * int(data[j].split(',')[0]))