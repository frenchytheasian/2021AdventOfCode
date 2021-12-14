from pprint import pprint
from operator import itemgetter

def parse_data():
    coords = []
    directions = []
    with open('in.txt', 'r') as f:
        data = f.read()
        coords_raw, directions_raw = data.split('\n\n')
        coords_raw = coords_raw.split('\n')
        for coord_raw in coords_raw:
            coord_raw = (coord_raw.strip().split(','))
            coord = []
            for val in coord_raw:
                coord.append(int(val))
            coords.append(coord)

        directions_raw = directions_raw.split('\n')
        for direction_raw in directions_raw:
            direction_raw = direction_raw.split('along ')[1]
            axis, value = direction_raw.split('=')
            directions.append([axis, int(value)])

    return coords, directions  

def fold(paper, instruction):
    axis_index = None
    fold_amount = instruction[1]
    folded_paper = []
    if instruction[0] == 'y':
        axis_index = 1
    else:
        axis_index = 0
    
    for i, coord in enumerate(paper):
        if coord[axis_index] > fold_amount:
            # Calculate the new position of a folded coordinate
            coord[axis_index] = fold_amount - (coord[axis_index] - fold_amount)
            # Only keep value if it's unique
            if coord not in folded_paper:
                folded_paper.append(coord)
        else:
            if coord not in folded_paper:
                folded_paper.append(coord)
    
    return folded_paper

def print_letters(paper):
    maxX = paper[-1][0]
    maxY = max(paper, key=itemgetter(1))[1]
    
    grid = []
    string_grid = ''

    # Create an empty grid
    for i in range(maxY + 1):
        grid.append([' ' for x in range(maxX + 1)])

    # Mark filled spots with a readable value
    for val in paper:
        x, y = val[0], val[1]
        grid[y][x] = 'x'
    
    # Turn grid into a printable string
    for row in grid:
        row.append('\n')
        string_grid += ''.join(row)
    print(string_grid)



def main():
    coords, directions = parse_data()
    for i, direction in enumerate(directions):
        coords = fold(coords, directions[i])
    coords = sorted(coords, key=itemgetter(0, 1))
    print_letters(coords)
    

if __name__ == "__main__":
    main()