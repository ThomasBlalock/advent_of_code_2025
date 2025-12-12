#%%
with open('data/day9.txt', 'r') as file:
    data = file.read()
data = data.split('\n')

# Puzzle 1
max_area = 0
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        x1, y1 = [int(k) for k in data[i].split(',')]
        x2, y2 = [int(k) for k in data[j].split(',')]
        area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
        if area > max_area:
            max_area = area
print(max_area)


# Puzzle 2
def line_intersects(xi1, yi1, xi2, yi2, 
                    xj1, yj1, xj2, yj2):
    s = False
    if xj1 == xj2:
        if xi1 < xj1 < xi2 and yj1 < yi1 < yj2:
            s = True
            intersect_coords = (xj1, yi1)
    else: # yj1 == yj2:
        if yi1 < yj1 < yi2 and xj1 < xi1 < xj2:
            s = True
            intersect_coords = (xi1, yj1)
    if s:
        return intersect_coords
    else:
        return None
            

max_area = 0
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        x1, y1 = [int(k) for k in data[i].split(',')]
        x2, y2 = [int(k) for k in data[j].split(',')]
        sides = [
            (x1, y1, x1, y2),
            (x1, y2, x2, y2),
            (x2, y2, x2, y1),
            (x2, y1, x1, y1),
        ]
        
        for k in range(len(data)):
            xkp, ykp = [int(o) for o in data[k-1].split(',')]
            xk, yk = [int(o) for o in data[k].split(',')]
            for side in sides:
                x1s, y1s, x2s, y2s = side
                r = line_intersects(x1s, y1s, x2s, y2s,
                                xkp, ykp, xk, yk)
                if r:
                    break
            else:
                continue
            break
        else:
            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            if area > max_area:
                max_area = area

print(max_area) # x < 3980792801