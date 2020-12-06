import numpy as np
from itertools import combinations

def multiply_entries(array, n_entries):
    values = None
    for combi in combinations(array, n_entries):
        if sum(combi) == 2020:
            values = combi
            break
    return np.prod(values)

if __name__ == '__main__':
    path_to_data_file = '../data/day1_data.txt'

    data = np.genfromtxt(path_to_data_file, dtype=int)

    product_two = multiply_entries(data, 2)
    product_three = multiply_entries(data, 3)

    ### Part 1
    print(f"The multiplication of two entries that sum to 2020 is equal to {product_two}.")
    ### Part 2
    print(f"The multiplication of three entries that sum to 2020 is equal to {product_three}.")
