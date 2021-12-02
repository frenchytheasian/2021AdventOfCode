def calc_position(file):
    horizontal = 0
    depth = 0
    aim = 0

    for line in file:
        temp = line.split()
        command = temp[0]
        amount = int(temp[1].strip())
        if command == "forward":
            horizontal += amount
            depth += (aim*amount)
        elif command == "up":
            aim -= amount
        else:
            aim += amount
        
    return depth * horizontal

def main():
    with open("day2.txt", "r") as f:
        ans = calc_position(f)
    
    print(ans)

if __name__ == "__main__":
    main()
