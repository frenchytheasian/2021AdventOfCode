"""Used solutions to help me solve this"""

from collections import defaultdict
from pprint import pprint
from typing import List

def parse_data():
    cave_map = defaultdict(list)

    with open("in.txt", 'r') as f:
        for line in f:
            line_split = line.strip().split('-')
            cave_map[line_split[0]].append(line_split[1])
            cave_map[line_split[1]].append(line_split[0])
    return cave_map

def traverse(caves: List, cave: str, visited, two_visits):

    if visited[cave] > 0 and two_visits:
        return 0
    elif cave == "end":
        return 1
    if cave.islower():
        visited[cave] += 1
        if visited[cave] == 2:
            two_visits = True

    ans = 0

    for adj_cave in caves[cave]:
        if adj_cave != "start":
            ans += traverse(caves, adj_cave, visited, two_visits)

    if cave.islower():
        visited[cave] -= 1

    
    return ans

def main():
    caves = parse_data()
    print(traverse(caves, 'start', defaultdict(int), False))

if __name__ == "__main__":
    main()