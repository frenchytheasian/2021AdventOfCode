from typing import List
from pprint import pprint

def oxygen_rating(array: list):
    
    max = ""
    index = 0

    while len(array) > 1:
        temp_array = []
        one_count = 0
        for row in array:
            if row[index] == "1":
                one_count += 1
        if one_count >= len(array)/2:
            max = "1"
        else: 
            max = "0"
        for row in array:
            if row[index] == max:
                temp_array.append(row)
        array = temp_array
        index += 1
    return array

def carbon_rating(array: list):
    
    min = ""
    index = 0

    while len(array) > 1:
        temp_array = []
        one_count = 0
        zero_count = 0
        for row in array:
            if row[index] == "1":
                one_count += 1
            if row[index] == "0":
                zero_count += 1
        if one_count < zero_count:
            min = "1"
        else: 
            min = "0"
        for row in array:
            if row[index] == min:
                temp_array.append(row)
        array = temp_array
        index += 1
    return array


def create_array(filename:str):
    array = []

    with open(filename, 'r') as f:
        for line in f:
            row = list(line.strip())
            array.append(row)
    return array

def main():
    array = create_array("day3.txt")
    oxygen = int(''.join(oxygen_rating(array)[0]), 2)
    carbon = int(''.join(carbon_rating(array)[0]), 2)
    print(oxygen*carbon)
    

if __name__ == "__main__":
    main()