import pandas as pd

def find_accumulator(df):
    accumulator = 0
    index = 0
    once_index = set()
    continue_cycle = True

    while continue_cycle:
        if index in once_index:
            return accumulator
        row = df.loc[index, :]
        once_index.add(index)
        if row.operation == 'acc':
            if row.sign == '+':
                accumulator += row.value
            else:
                accumulator -= row.value
            index += 1
        elif row.operation == 'jmp':
            if row.sign == '+':
                index += row.value
            else:
                index -= row.value
        elif row.operation == 'nop':
             index += 1

def find_accumulator_corrected(df):
    for ind_to_replace in df[df.operation.isin(['jmp', 'nop'])].index:
        accumulator = 0
        index = 0
        once_index = set()
        continue_cycle = True
        while continue_cycle:
            if index in once_index:
                continue_cycle = False
                break
            if index == len(df)-1:
                return accumulator
            row = df.loc[index, :].copy()
            if index == ind_to_replace:
                if row.operation == 'jmp':
                    row.operation = 'nop'
                elif row.operation == 'nop':
                    row.operation = 'jmp'
            once_index.add(index)
            if row.operation == 'acc':
                if row.sign == '+':
                    accumulator += row.value
                else:
                    accumulator -= row.value
                index += 1
            elif row.operation == 'jmp':
                if row.sign == '+':
                    index += row.value
                else:
                    index -= row.value
            elif row.operation == 'nop':
                 index += 1


if __name__ == '__main__':

    path_to_data_file = '../data/day8_data.txt'
    data = []
    with open(path_to_data_file, 'r') as f:
        for line in f:
            splitted = line.split()
            data.append([splitted[0], splitted[-1][0], int(splitted[-1][1:])])
    df_day8 = pd.DataFrame(data, columns=['operation', 'sign', 'value'])

    accumulator = find_accumulator(df_day8)
    print(f'In the accumulator is {accumulator}.')

    corrected_accumulator = find_accumulator_corrected(df_day8)
    print(f'The value of the accumulator after the program terminates is {corrected_accumulator}.')
