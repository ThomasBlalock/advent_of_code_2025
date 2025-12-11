#%%
with open('data/day6.txt', 'r') as file:
    data = file.read()
data = data.split('\n')
data = [
    [
        n.replace(' ', '')
        for n in d.split(' ')
        if n != ''
    ] 
    for d in data
]

# Puzzle 1
ttl = 0
def mult(x):
    if not x:
        return 0
    result = 1
    for i in x:
        result *= i
    return result

for i in range(len(data[-1])):
    op = lambda x: sum(x) if data[-1][i]=='+' else mult(x)
    nums = [int(data[j][i]) for j in range(len(data)-1)]
    ttl += op(nums)
print(ttl)


# Puzzle 2
ttl = 0
with open('data/day6.txt', 'r') as file:
    data = file.read()
data = data.split('\n')
ops = data[-1]
data = data[:-1]

j = 0
for i in range(len(ops)):
    op = lambda x: sum(x) if ops[i]=='+' else mult(x)
    nums = []

    first = True
    row_of_blanks = True
    while (not row_of_blanks or first) and j < len(data[0])+1:
        r = ''
        row_of_blanks = True
        for x in range(len(data)):
            try:
                if data[x][j] == ' ':
                    continue
            except IndexError:
                j += 1
                continue
            r += data[x][j]
            row_of_blanks = False
        if not row_of_blanks and first:
            first = False
        if not row_of_blanks:
            nums.append(int(r))
        j += 1
    if nums:
        ttl += op(nums)
print(ttl) # 329632715776 < x < 11327104040927165