
"""
Name: Random Set Generator
Author: Luke Atkins
Purpose: This program will generate 100 random numbers 1-10, print the total elements, and the average.
Starter Code: No starter code used
Date: 2/3/2026
"""

from random import randint

def main():
    # create 100 random numbers 1-10
    numbers = [randint(1, 10) for _ in range(100)]
    # total
    total = sum(numbers)
    avg = total / len(numbers)
    # print
    print(f"Total of all numbers in list: {total}")
    print(f"Average of numbers: {avg}")

if __name__ == "__main__":
    main()