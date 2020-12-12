import re

def colors_in_bag(path_to_data_file, bag_color):
    new_bags = set([bag_color])
    old_bags = set()
    is_different = True

    while is_different:
        old_bags = new_bags.copy()
        with open(path_to_data_file, 'r') as f:
            for line in f:
                splitted = line.split('bags contain')
                for bag in old_bags:
                    if bag in splitted[-1]:
                        new_bags.add(splitted[0])
                        break
            if len(old_bags) == len(new_bags):
                is_different = False

    new_bags.remove(bag_color)
    return len(new_bags)

def bags_inside_single_bag(path_to_data_file, bag_color):
    regex = r"\s?(?P<value>[0-9]{1,2})\s(?P<note>\w+\s{1}\w+) bag"
    out_bags = set()
    in_bags = set([bag_color])
    all_colors_previous = dict()
    all_colors_next = {bag_color: 1}
    is_full = True
    value = 0

    while is_full:
        out_bags = in_bags.copy()
        all_colors_previous = all_colors_next.copy()
        in_bags = set()
        all_colors_next = dict()
        with open(path_to_data_file, 'r') as f:
            for ind, line in enumerate(f):
                splitted = line.split('bags contain')
                for bag in out_bags:
                    if bag in splitted[0]:
                        if 'no other bags' in splitted[-1]:
                            out_bags.remove(bag)
                        else:
                            for each in re.findall(regex, splitted[-1]):
                                in_bags.add(each[-1])
                                if each[-1] in all_colors_next.keys():
                                    all_colors_next[each[-1]] += all_colors_previous.get(bag) * int(each[0])
                                else:
                                    all_colors_next[each[-1]] = all_colors_previous.get(bag) * int(each[0])
                        break
            value += sum(all_colors_next.values())
            if not out_bags:
                is_full = False
    return value


if __name__ == '__main__':
    path_to_data_file = '../data/day7_data.txt'
    bag_color = 'shiny gold'
    n_bags = colors_in_bag(path_to_data_file, bag_color)
    print(f'{n_bags} bag colors can contain at least one {bag_color} bag.')

    value = bags_inside_single_bag(path_to_data_file, bag_color)
    print(f'{value} individual bags are required inside a single {bag_color} bag.')
