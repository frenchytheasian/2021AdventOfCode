from pprint import pprint
from math import inf, prod

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
                lows.append((i, j))
    return lows

def get_basin(heightmap, row, col, basin_size):
    if heightmap[row][col] >= 9:
        return 0
    else:
        basin_size.append(heightmap[row][col])
        heightmap[row][col] = inf
        get_basin(heightmap, row+1, col, basin_size)
        get_basin(heightmap, row, col+1, basin_size)
        get_basin(heightmap, row-1, col, basin_size)
        get_basin(heightmap, row, col-1, basin_size)
    return len(basin_size)
    
    

def main():
    heightmap = parse_data()
    lows = find_low(heightmap)
    basin_size = []
    for low in lows:
        basin_size.append(get_basin(heightmap, low[0], low[1], []))
        
    ans = prod(sorted(basin_size)[-3:])
    print(ans)

if __name__ == "__main__":
    main()