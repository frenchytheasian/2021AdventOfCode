

def parse_data():
    with open('day7.txt', 'r') as f:
        positions = f.read().strip().split(',')
        for i, position in enumerate(positions):
            positions[i] = int(position)
        return positions

def find_energy_costs(positions):
    costs = []
    for i in range(max(positions)):
        temp_sum = sum([((abs(position - i)*(abs(position - i) + 1))//2) for position in positions])
        costs.append(temp_sum)
    return costs

def main():
    data = parse_data()

    # For Part 1
    costs = find_energy_costs(data)
    print(min(costs))


if __name__ == "__main__":
    main()