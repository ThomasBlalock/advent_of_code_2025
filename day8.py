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

class Node:
    def __init__(self):
        self.connected = []
graph = [Node() for _ in range(len(data))]
for _ in range(1000):
    dist, i, j = heapq.heappop(heap)
    graph[i].connected.append(j)
    graph[j].connected.append(i)

visited = set()
circuits = []
for i in range(len(graph)):
    if i in visited:
        continue
    stack = [i]
    circuit = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        circuit.add(node)
        for neighbor in graph[node].connected:
            if neighbor not in visited:
                stack.append(neighbor)
    circuits.append(circuit)

circuit_sizes = sorted([len(circuit) for circuit in circuits], reverse=True)
print(circuit_sizes[0]*circuit_sizes[1]*circuit_sizes[2])
