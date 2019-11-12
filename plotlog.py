import numpy
import os
import matplotlib.pyplot as plt


f = open("PythonTestScript.txt", "r")
lines = f.read().splitlines()
f.close()


def find_index(start_idx, substring):
    global lines
    for index, line in enumerate(lines[start_idx:]):
        if substring in line:
            print("yay!")
            return index+1


def main():
    start_idx = 0
    start_idx = find_index(start_idx, "Query Received")
    end_idx = find_index(start_idx, "Waiting for the event")
    desired_lines = lines[start_idx : (start_idx + end_idx - 1)]
    print(desired_lines)

if __name__ == "__main__":
    main()
