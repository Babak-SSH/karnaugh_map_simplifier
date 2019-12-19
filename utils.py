def binary_code(num):
    binary_value = format(num, 'b')
    binary_list = list(map(int, binary_value.split()))

def is_joinable(group1, group2):
    diff_count = 0
    diff_index = 0
    for i in range(group1[0]):
        if (group1[2][i] != group2[2][i]):
            diff_index = i
            diff_count += 1
    if (diff_count == 1):
        return diff_index
    return 0

def is_inside_group(i, j, g, k_map_index):
    cell_binary = binary_code(k_map_index[i][j])
    for i in range(len(cell_binary)):
        if (cell_binary[i] != g[2][i] and g[2][i] != 2):
            return False
    return True

def is_coverd(groups, group, height, width):
    k_map_temp = [[0 for _ in range(width)]*height]
    for g in groups:
        if (g != groups):
            for i in range(height):
                for j in range(width):
                    if (is_inside_group(i, j, g, k_map_index)):
                        k_map_temp[i][j] = 1
    return k_map == k_map_temp
