def parse_data():
    stages = [0]*9
    with open('day6.txt', 'r') as f:
        ages_raw = f.read().strip().split(',')
    for age in ages_raw:
        stages[int(age)] += 1
    return stages

def day(ages):
    birthers = ages.pop(0)
    ages[6] += birthers
    ages.append(birthers)

def main():
    ages = parse_data()
    for _ in range(256):
        day(ages)
    print(sum(ages))



if __name__ == "__main__":
    main()