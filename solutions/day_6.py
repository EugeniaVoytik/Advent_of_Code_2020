from collections import Counter

def positive_answered_questions(file):
    all_answers = 0
    with open(file, 'r') as f:
        combined_string = ''
        for line in f:
            actual_line = line.strip()
            if len(actual_line) > 0:
                combined_string += actual_line
            else:
                all_answers += len(set(combined_string))
                combined_string = ''
        all_answers += len(set(combined_string))
    return all_answers


def positive_answered_questions_by_all_members(file):
    all_positive_answers = 0
    with open(file, 'r') as f:
        combined_string = ''
        num_people = 0
        for line in f:
            actual_line = line.strip()
            if len(actual_line) > 0:
                num_people += 1
                combined_string += actual_line
            else:
                all_positive_answers += sum(
                    [True if letter == num_people else False for letter in Counter(combined_string).values()])
                combined_string = ''
                num_people = 0
        all_positive_answers += sum([True if letter == num_people else False for letter in Counter(combined_string).values()])
    return all_positive_answers


if __name__ == '__main__':
    path_to_data_file = '../data/day6_data.txt'
    all_answers = positive_answered_questions(path_to_data_file)
    all_positive_answers = positive_answered_questions_by_all_members(path_to_data_file)

    ### Part 1
    print(f"The number of answered 'yes' questions is {all_answers}.")
    ### Part 2
    print(f"The number of answered 'yes' questions by all members in the group is {all_positive_answers}.")
