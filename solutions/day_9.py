from itertools import combinations

def find_first_invalid_number(path_to_data_file, preamble_len):
    values = []
    first_number = 0
    with open(path_to_data_file, 'r') as f:
        for ind, line in enumerate(f):
            current_value = int(line.strip())
            values.append(current_value)
            if ind > preamble_len:
                all_sums = set()
                for combi in combinations(values[-preamble_len-1:-1], 2):
                    all_sums.add(sum(combi))
                if current_value not in all_sums:
                    first_number = current_value
    return first_number, values


def find_contiguous_set(values):
    # starting from 1 because a contiguous set should have at least two numbers
    for i in range(1, len(values)+1):
        current_sum = 0
        for j in range(i, len(values)+1):
            current_sum += values[j]
            if current_sum == first_number:
                return i, j+1
            elif current_sum > first_number:
                break

if __name__ == '__main__':

    path_to_data_file = '../data/day9_data.txt'
    preamble_len = 25

    first_number, values = find_first_invalid_number(
        path_to_data_file,
        preamble_len
    )
    print(f'The first number that does not have this property is {first_number}.')

    i, j = find_contiguous_set(values)
    encryption_weakness = min(values[i:j]) + max(values[i:j])
    print(f'The encryption weakness in the XMAS-encrypted list of numbers is equal to {encryption_weakness}.')
