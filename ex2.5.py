import json
import random
import sys
import json
import time
import matplotlib.pyplot as plt
import threading
threading.stack_size(33554432)
sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
  
    return high

def main():
    file = open("ex2.5.json", "r")
    contents = json.load(file)
    inputSize = []
    timing = []

# Sort each input and measure the time taken
    for i, input_array in enumerate(contents):
        n = len(input_array)
        inputSize.append(n)
        start_time = time.time()
        func1(input_array, 0, n-1)
        end_time = time.time()
        timing.append(end_time - start_time)
    plt.plot(inputSize, timing, 'o-')
    plt.xlabel("Input Size")
    plt.ylabel("Sorting Time (s)")
    plt.title("Quick Sort Timing Results")
    plt.show()

main()