from pprint import pprint
from typing import List

def parse_data():
    data = []
    signals = []
    with open('day8.txt', 'r') as f:
        for line in f:
            line_raw = line.split('|')
            data.append(line_raw[1].strip().split(' '))
            signals.append(line_raw[0].strip().split(' '))
    
    return [data, signals]

def generateMap(signals):
    """
    Generate a dictionary of numbers corresponding to their values.
    This is done using set theory and finding complements of some known strings
    """
    known = dict()
    # initial loop to get easy numbers
    for string in signals:
        if len(string) == 2:
            known['1'] = string
        elif len(string) == 3:
            known['7'] = string
        elif len(string) == 4:
            known['4'] = string
        elif len(string) == 7:
            known['8'] = string
    signals.remove(known['1'])
    signals.remove(known['4'])
    signals.remove(known['7'])
    signals.remove(known['8'])

    # second loop with easy numbers known to find the rest of the values
    for string in signals:
        if len(string) == 6:
            if (set(known['8']) - set(string)).pop() in known['1']:
                known['6'] = string
            elif (set(known['8']) - set(string)).pop() in known['4']:
                known['0'] = string
            else:
                known['9'] = string
        if len(string) == 5:
            if not (set(known['1']) - set(string)):
                known['3'] = string
            elif len(set(known['4']) - set(string)) == 1:
                known['5'] = string
            else:
                known['2'] = string

    return known

def reverse_dict(map):
    """
    sort the strings and create a new dictionary
    """
    patterns = dict()
    for key, value in map.items():
        new_key = "".join(sorted(value))
        patterns[new_key] = key
    return patterns

def get_value(key: dict, nums: List) -> int:
    """[summary]

    Args:
        key (dict): [description]
        nums (List): [description]

    Returns:
        int: [description]
    """
    final_num = ""
    for digit in nums:
        query = "".join(sorted(digit))
        final_num += key[query]
    return int(final_num)


def main():
    data = parse_data()
    nums, signals = data[0], data[1]

    total = 0           # final answer
    for i, line in enumerate(nums):
        my_map = generateMap(signals[i])
        checker = reverse_dict(my_map)
        total += get_value(checker, nums[i])

    print(total)
        

if __name__ == "__main__":
    main()
