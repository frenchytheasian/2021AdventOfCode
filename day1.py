def number_of_increases(depths):
    num_increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            num_increases += 1

    return num_increases

def transform_list(depths):
    summed_depths = []
    for i in range(len(depths) - 2):
        summed_depths.append(sum(depths[i:i+3]))

    return summed_depths

def main():
    depths = []
    with open('day1.txt', 'r') as f:
        for line in f:
            num = int(line.strip())
            depths.append(num)
    
    depths = transform_list(depths)
    ans = number_of_increases(depths)
    print(ans)
            

if __name__ == "__main__":
    main()