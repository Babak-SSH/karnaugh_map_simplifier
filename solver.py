from math import ceil, floor, pow, log
from utils import binary_code, is_joinable, is_inside_group, is_covered


def make_karnaugh_map(variables_count, terms):
    #gray encode of each cell (it scale 4*4 to bigger values)
    gray_code = {0:0, 1:1, 2:3, 3:2, 4:4, 5:5, 6:7, 7:6, 8:12, 9:13, 10:15, 11:14, 12:8, 13:9, 14:11, 15:10}

    #k-map matrix with index values based on their gray code
    k_map_index = []

    #scale of the map
    width = int(pow(2, ceil(variables_count/2)))
    height = int(pow(2, floor(variables_count/2)))

    #this map is for grouping cells
    k_map = [[0 for _ in range(width)] for _ in range(height)]

    if (variables_count >= 3):
        k_map_index = [[gray_code[(j%4)+((i%4)*4)]+16*(j//4+((i//4)*(width//4))) for j in range(width)] for i in range(height)]
    elif(variables_count == 2):
        k_map_index = [[0,1], [2,3]]
    elif(variables_count == 1):
        k_map_index = [0,1]

    #specifyng the terms
    for i in range(height):
        for j in range(width):
            if (k_map_index[i][j] in terms):
                k_map[i][j] = 1

    return k_map_index, k_map

def solve(d_care, k_map_index, k_map, v_count):
    k_map_temp = k_map[:]
    width = len(k_map_index[0])
    height = len(k_map_index)
    c = 0

    #check all possible orders for gray code cells and find 
    #if we can reduce group numbers or make bigger groups.
    for d in range(int(pow(2, len(d_care)))):
        d_care_order = binary_code(d, v_count)
        for i in range(height):
            for j in range(width):
                if (k_map_index[i][j] in d_care):
                    if (d_care_order[c] == 1):
                        k_map_temp[i][j] = 1
                        c += 1

    groups = solve_groups(k_map_index, k_map_temp, v_count)

    print(groups)
    return groups

def solve_groups(k_map_index, k_map, v_count):
    width = len(k_map_index[0])
    height = len(k_map_index)
    groups = []

    #check special cases(all of them 1 or 0).
    if (all([x == k_map[0][0] for r in k_map for x in r])):
        if (k_map[0][0] == 1):
            return 1
        elif (k_map[0][0] == 0):
            return 0

    #getting all groups with 1 cell.
    for i in range(height):
        for j in range(width):
            if (k_map[i][j] == 1):
                groups.append([1, 0, binary_code(k_map_index[i][j], v_count)])
                
    #getting all groups with 2^i cells.
    for i in range(0, int(log(height*width, 2))+1):
        new_groups = []
        for g1 in groups:
            for g2 in groups:
                if (g1[0] == pow(2, i) and g2[0] == pow(2, i)):
                    diff = is_joinable(g1, g2)

                    if (diff != -1):
                        #if this two are joinable we make new block out of them.
                        group = [0, 0, []]
                        g1[1] = 1
                        g2[1] = 1
                        
                        group[0] = 2*g1[0]
                        group[1] = 0
                        group[2] = g1[2][:]
                        group[2][diff] = 2

                        if (all([group[2] != g[2] for g in new_groups])):
                            new_groups.append(group)
        groups += new_groups
    print(groups)

    #removing groups that are part of bigger groups
    groups = [g for g in groups if g[1] != 1]
    print(groups)

    if (len(groups) == 1):
        return groups

    #removing groups which is covered by other groups and there is no need to save them.
    #groups = [g for g in groups if is_covered(groups, g, height, width, k_map, k_map_index, v_count)]
    essential_groups = []
    extra_groups = []
    for g in groups:
        if (is_covered(groups, g, height, width, k_map, k_map_index, v_count, extra_groups)):
            essential_groups.append(g)
        else:
            extra_groups.append(g)

    return groups

