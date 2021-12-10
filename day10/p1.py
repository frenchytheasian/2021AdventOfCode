def parse_data():
    data = []
    with open('in.txt', 'r') as f:
        for line in f:
            line = line.strip()
            data.append(line)
    return data

def error_score(line):
    pairs = {'[': ']', '(': ')', '{': '}', '<': '>'}
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    waiting = []
    for char in line:
        if char in ['[', '(', '{', '<']:
            waiting.append(pairs[char])
        else: 
            if char == waiting.pop():
                continue
            else:
                return score[char]
    return 0

def main():
    subsystem = parse_data()
    score = 0
    for line in subsystem:
        score += error_score(line)
    print(score)

if __name__ == "__main__":
    main()