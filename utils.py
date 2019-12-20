def binary_code(num, v_count):
    binary_value = format(num, 'b')
    binary_list = [int(x) for x in binary_value]
    while (len(binary_list) != v_count):
        binary_list.insert(0, 0)
    return binary_list

def is_joinable(group1, group2):
    diff_count = 0
    diff_index = 0
    for i in range(len(group1[2])):
        if (group1[2][i] != group2[2][i]):
            diff_index = i
            diff_count += 1
    if (diff_count == 1):
        return diff_index
    return -1

def is_inside_group(i, j, g, k_map_index, v_count):
    cell_binary = binary_code(k_map_index[i][j], v_count)
    for i in range(len(cell_binary)):
        if (cell_binary[i] != g[2][i] and g[2][i] != 2):
            return False
    return True

def is_covered(groups, group, height, width, k_map, k_map_index, v_count, extra):
    k_map_temp = [[0 for _ in range(width)] for _ in range(height)]
    for g in groups:
        if ((g != group) and g not in extra):
            for i in range(height):
                for j in range(width):
                    if (is_inside_group(i, j, g, k_map_index, v_count)):
                        k_map_temp[i][j] = 1
    return k_map != k_map_temp
