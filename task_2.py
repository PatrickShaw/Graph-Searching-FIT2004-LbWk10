__author__ = "Patrick Shaw"


def read_substrings():
    substrings = []
    with open("substrings1.txt") as input_file:
        for line in input_file:
            substrings.append(line.strip())
    return substrings


print(read_substrings())
