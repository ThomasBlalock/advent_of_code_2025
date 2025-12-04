#%%
with open('data/day1.txt', 'r') as file:
    data = file.read()
data = data.replace('L', '-').replace('R', '').split('\n')
data = [int(x) for x in data[:-1]]

# Puzzle 1
ptr = 50
ttl = 0
for i in data:
    if ptr==0:
        ttl += 1
    ptr = (ptr + i) % 100
print(ttl)

# Puzzle 2
ptr = 50
ttl = 0
for i in data:
    start_ptr = ptr
    ptr += (abs(i) % 100) * (abs(i)/i)
    ttl += int(abs(i)/100)
    if (ptr<=0) and (i%100!=0) and start_ptr!=0:
        ttl += + 1
    elif (ptr>=100) and (i%100!=0):
        ttl += 1
    ptr = ptr % 100
print(ttl)