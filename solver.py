from math import ceil, floor, pow
from utils import binary_code


def make_karnaugh_map(variables_count, terms):
    #gray encode of each cell (it scale 4*4 to bigger values)
    gray_code = {0:0, 1:1, 2:3, 3:2, 4:4, 5:5, 6:7, 7:6, 8:12, 9:13, 10:15, 11:14, 12:8, 13:9, 14:11, 15:10}
    #k-map matrix with index values
    k_map_index = []

    #scale of the map
    width = int(pow(2, ceil(variables_count/2)))
    heigth = int(pow(2, floor(variables_count/2)))

    k_map = [[0 for _ in range(width)] * height]

    if (variables_count >= 3):
        k_map_index = [[gray_code[(j%4)+((i%4)*4)]+16*(j//4+((i//4)*(width//4))) for j in range(width)] for i in range(heigth)]
    elif(variables_count == 2):
        k_map_index = [[0,1], [2,3]]
    elif(variables_count == 1):
        k_map_index = [0,1]

    for i in range(len(height)):
        for j in range(len(width)):
            if (k_map_index[i][j] in terms):
                k_map[i][j] = 1

    return k_map_index, k_map

def solve(d_care, k_map_index, k_map):
    k_map_temp = k_map[:]
    width = len(k_map_index[0])
    height = len(k_map_index)
    c = 0
    #check all possible orders for gray code cells and find 
    #if we can reduce group numbers or make bigger groups.
    for d in range(pow(2, len(d_care))):
        d_care_order = binary_code(d)
        for i in range(height):
            for j in range(width):
                if (k_map_index[i][j] in d_care):
                    if (d_care_order[c] == 1):
                        k_map_temp[i][j] = 1
                        c += 1

    solve_groups(k_map_index, k_map_temp)

def solve_groups(k_map_index, k_map):
    width = len(k_map_index[0])
    height = len(k_map_index)
    groups = []

    #check special cases(all of them 1 or 0)
    if (all([x == k_map[0][0] for r in k_map for x in r])):
        if (k_map[0][0] == 1):
            return 1
        elif (k_map[0][0] == 0):
            return 0

    for i in range(height):
        for j in range(width):
            if (k_map[i][j] == 1):
                group = [1, 0, binary_code(k_map_index[i][j])]
                groups.append(group)
