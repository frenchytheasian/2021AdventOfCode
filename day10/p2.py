def parse_data():
    data = []
    with open('in.txt', 'r') as f:
        for line in f:
            line = line.strip()
            data.append(line)
    return data

def get_completion_strings(line):
    pairs = {'[': ']', '(': ')', '{': '}', '<': '>'}
    waiting = []
    for char in line:
        if char in ['[', '(', '{', '<']:
            waiting.append(pairs[char])
        else: 
            if char == waiting.pop():
                continue
            else:
                return []
    return waiting

def calculate_line_score(line):
    score = 0
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    for char in line:
        score *= 5
        score += scores[char]
    return score

def main():
    subsystem = parse_data()

    # Filter out the corrupted strings and return the completion
    # strings of the incomplete lines
    completion_strings = []
    for line in subsystem:
        completion_string = get_completion_strings(line)
        if completion_string:
            completion_string.reverse()
            completion_strings.append(completion_string)
    
    # Calculate the scores of all the completion strings
    line_scores = []
    for string in completion_strings:
        line_scores.append(calculate_line_score(string))

    # Get the middle value of the final scores
    ans = sorted(line_scores)[len(line_scores)//2]
    print(ans)
        
    


if __name__ == "__main__":
    main()