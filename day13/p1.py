from pprint import pprint

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
            coord[axis_index] = fold_amount - (coord[axis_index] - fold_amount)
            if coord not in folded_paper:
                folded_paper.append(coord)
        else:
            if coord not in folded_paper:
                folded_paper.append(coord)
    
    return folded_paper

def main():
    coords, directions = parse_data()
    paper = fold(coords, directions[0])
    pprint(paper)
    print(len(paper))

if __name__ == "__main__":
    main()