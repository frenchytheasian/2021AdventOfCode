from pprint import pprint


def parse_data():
    data = 0
    with open('day8.txt', 'r') as f:
        for line in f:
            line = line.split('|')[1].strip()
            strings = line.strip().split(' ')
            for chars in strings:
                if len(chars) in [2,3,4,7]:
                    data += 1
    
    return data

def main():
    nums = parse_data()
    pprint(nums)

if __name__ == "__main__":
    main()
