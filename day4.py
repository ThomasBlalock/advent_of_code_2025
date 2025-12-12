#%%
with open('data/day4.txt', 'r') as file:
    data = file.read()
data = data.split('\n')


# Puzzle 1
ttl = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '@':
            continue
        num_surrounding = 0
        for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1),
                     (i, j-1),              (i, j+1),
                     (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if x<0 or y<0:
                continue
            try:
                if data[x][y] == '@':
                    num_surrounding += 1
            except IndexError:
                continue
        if num_surrounding < 4:
            ttl += 1
print(ttl)


# Puzzle 2
ttl = 0
while True:
    ttl_add = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '@':
                continue
            num_surrounding = 0
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),              (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if x<0 or y<0:
                    continue
                try:
                    if data[x][y] == '@':
                        num_surrounding += 1
                except IndexError:
                    continue
            if num_surrounding < 4:
                ttl_add += 1
                data[i] = data[i][:j] + '.' + data[i][j+1:]

    ttl += ttl_add
    if ttl_add == 0:
        break
print(ttl)
