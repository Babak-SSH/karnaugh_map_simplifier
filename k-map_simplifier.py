from solver import make_karnaugh_map, solve


def get_inputs():
    variables_count = int(input())
    #TODO get maxterms too
    terms = list(map(int, input().split()))
    d_cares = list(map(int, input().split()))
    return variables_count, terms, d_cares

if __name__ == "__main__":
    variables_count, terms, d_care = get_inputs()
    k_map_index, k_map = make_karnaugh_map(variables_count, terms)
    solve(d_care, k_map_index, k_map, variables_count)
