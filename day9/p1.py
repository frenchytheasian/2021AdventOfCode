from pprint import pprint
from math import inf

def parse_data():
    with open('in.txt', 'r') as f:
        data = []
        for i, line in enumerate(f):
            temp = list(line.strip())
            data.append([int(x) for x in temp])

            # surround the data with infinities
            data[i].insert(0, inf)
            data[i].append(inf)

        # surround the data with infinities
        multiplier = len(data[0])
        dummy = [inf]*multiplier
        data.insert(0, dummy)
        data.append(dummy)

    return data

def find_low(heightmap):
    """
    Iterate through map and keep track of lows
    """
    lows = []
    for i in range(1, len(heightmap)-1):
        for j in range(1, len(heightmap[0])-1):
            if heightmap[i][j] < heightmap[i+1][j] and heightmap[i][j] < heightmap[i][j+1] and heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i][j-1]:
                lows.append(heightmap[i][j] + 1)
    return lows
    

def main():
    heightmap = parse_data()
    lows = find_low(heightmap)
    print(sum(lows))

if __name__ == "__main__":
    main()