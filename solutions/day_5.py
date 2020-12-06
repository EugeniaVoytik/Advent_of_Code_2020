def find_seat(boarding_pass, n_rows, n_columns):
    current_row = list(range(0, n_rows))
    current_column = list(range(0, n_columns))
    for each in boarding_pass:
        if each in ['F', 'B']:
            # to find a row
            value = len(current_row) // 2
            if each == 'F':
                current_row = current_row[:value]
            else:
                current_row = current_row[value:]
        else:
            # to find a column
            value = len(current_column) // 2
            if each == 'L':
                current_column = current_column[:value]
            else:
                current_column = current_column[value:]
    seat_id = current_row[0] * 8 + current_column[0]
    return seat_id


if __name__ == '__main__':
    path_to_data_file = '../data/day5_data.txt'
    n_rows = 128
    n_columns = 8

    seat_ids = []
    with open(path_to_data_file, 'r') as f:
        for line in f:
            seat_ids.append(find_seat(line, n_rows, n_columns))
    seat_ids = sorted(seat_ids)

    ### Part 1
    print(f"Maximal seat ID is {max(seat_ids)}.")
    ### Part 2
    print(f"My seat ID is {sum(range(seat_ids[0], seat_ids[-1]+1)) - sum(seat_ids)}.")
