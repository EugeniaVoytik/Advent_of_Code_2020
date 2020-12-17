def read_return_sorted(path_to_data_file):
    values = []
    with open(path_to_data_file, 'r') as f:
        for ind, line in enumerate(f):
            current_value = int(line.strip())
            values.append(current_value)
    # to add the charging outlet near your seat(an effective joltage rating = 0)
    # and a built-in joltage adapter (+3 jolts to the highest value)
    values.extend([0, max(values)+3])
    values_sorted = sorted(values)
    return values_sorted

def find_differences(values_sorted):
    diff_1 = diff_2 = diff_3 = 0
    for i in range(1, len(values_sorted)):
        diff = values_sorted[i] - values_sorted[i-1]
        if diff == 1:
            diff_1 += 1
        elif diff == 2:
            diff_2 += 1
        else:
            diff_3 += 1
    return diff_1, diff_2, diff_3


if __name__ == '__main__':

    path_to_data_file = '../data/day10_data.txt'
    values_sorted = read_return_sorted(path_to_data_file)

    diff_1, diff_2, diff_3 = find_differences(values_sorted)
    print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences is equal to {diff_1 * diff_3}.")

    cache = {}
    def fun(n):
        if n not in values_sorted:
            return 0
        elif values_sorted.index(n) == len(values_sorted)-2:
            return 1
        elif n in cache.keys():
            return cache[n]
        else:
            cache[n] = fun(n+1) + fun(n+2) + fun(n+3)
            return cache[n]

    print(f"the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device is {fun(0)}.")
