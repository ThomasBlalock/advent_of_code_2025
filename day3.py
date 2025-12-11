#%%
with open('data/day3.txt', 'r') as file:
    data = file.read()
data = data.split('\n')

# Puzzle 1
ttl = 0
for bank in data:

    max_10s = -1
    max_10s_idx = -1
    for i in range(len(bank)-1):
        digit = int(bank[i])
        if digit > max_10s:
            max_10s = digit
            max_10s_idx = i
    
    max_1s = -1
    for i in range(max_10s_idx+1, len(bank)):
        digit = int(bank[i])
        if digit > max_1s:
            max_1s = digit
    
    ttl += int(str(max_10s) + str(max_1s))
print(ttl)


# Puzzle 2
ttl = 0
for bank in data:

    r = ''
    max_idx = -1
    for i in range(11, -1, -1):
        max_num = -1
        for i in range(max_idx+1, len(bank)-i):
            digit = int(bank[i])
            if digit > max_num:
                max_num = digit
                max_idx = i
        r = r + str(max_num)
    
    ttl += int(r)
print(ttl)
