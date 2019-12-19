def binary_code(num):
    binary_value = format(num, 'b')
    binary_list = list(map(int, binary_value.split()))
