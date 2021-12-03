from typing import List
from pprint import pprint
from numpy import transpose


def generate_rates(array: List[List]):
    array = array.tolist()
    gamma = []
    epsilon = []
    for row in array:
        num_zeroes = row.count("0")
        num_ones = row.count("1")
        if num_ones >= num_zeroes:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    return (gamma, epsilon)


def create_array(filename:str):
    array = []

    with open(filename, 'r') as f:
        for line in f:
            row = list(line.strip())
            array.append(row)
    return transpose(array)

def main():
    array = create_array("day3.txt")
    rates = generate_rates(array)
    gamma = int(''.join(rates[0]), 2)
    epsilon = int(''.join(rates[1]), 2)
    print(gamma*epsilon)

if __name__ == "__main__":
    main()