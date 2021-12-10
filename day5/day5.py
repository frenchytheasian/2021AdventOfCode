from os import remove
from pprint import pprint

def parse_data():
    coords = []
    with open("day5.txt", 'r') as f:
        for line in f:
            raw_coords = line.strip().split('->')
            path = []
            for raw_coord in raw_coords:
                raw_nums = raw_coord.split(',')
                path.append((int(raw_nums[0]), int(raw_nums[1])))
            coords.append(path)
    return(coords)

def remove_diagonals(paths):
    new_path = []
    diagonals = []
    for path in paths:
        if (path[0][0] == path[1][0]) or (path[0][1] == path[1][1]):
            new_path.append(path)
        else:
            if path[0][0] > path[1][0]:
                path[0], path[1] = path[1], path[0]
            diagonals.append(path)
    return (new_path, diagonals)

def create_graph(paths):
    graph = [([0]*1000) for i in range(1001)]
    return graph
    
def mark_graph(paths, graph):
    count = 0

    for path in paths:
        xVals = (path[0][0], path[1][0])
        yVals = (path[0][1], path[1][1])

        minX, maxX = min(xVals), max(xVals)
        minY, maxY = min(yVals), max(yVals)

        for i in range(minX, maxX + 1):
            for j in range(minY, maxY + 1):
                graph[j][i] += 1
                if graph[j][i] == 2:
                    count += 1

    return (graph, count)

def mark_diagonals(paths, graph):
    count = 0

    for path in paths:
        x1, x2 = path[0][0], path[1][0]
        y1, y2 = path[0][1], path[1][1]
        slope = (y2-y1)/(x2-x1)
        
        x, y = x1, y1
        while x <= x2:
            graph[y][x] += 1
            if graph[y][x] == 2:
                count += 1
            x += 1
            if slope > 0:
                y += 1
            else:
                y -= 1
    return count

    

def main():
    paths = parse_data()
    paths, diagonals = remove_diagonals(paths)[0], remove_diagonals(paths)[1]
    graph = create_graph(paths)
    data = mark_graph(paths,graph)
    graph, count = data[0], data[1]
    count += mark_diagonals(diagonals, graph)
    print(count)

if __name__ == "__main__":
    main()