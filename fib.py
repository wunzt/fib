# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/19/2022
# Description: Function takes a positive integer and returns the number at that position in a Fibonacci sequence.

def fib(seq):
    """Takes a positive integer parameter and returns the number at that position of the Fibonacci sequence."""
    num_1 = 1
    num_2 = 1
    for num in range(3, seq + 1):
        num_3 = num_1 + num_2
        num_1 = num_2
        num_2 = num_3
    return num_2