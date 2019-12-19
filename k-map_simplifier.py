from solver import make_karnaugh_map


def get_inputs():
    variables_count = int(input())
    #TODO get maxterms too
    minterms = list(map(int, input().split()))
    dcares = list(map(int, input().split()))
    return variables_count, d_cares

if __name__ == "__main__":
    variables, d_care = get_inputs()
    k_map_index = make_karnaugh_map(variables)
