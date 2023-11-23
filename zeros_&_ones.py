#You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
import numpy as np

n = list(map(int, input().split()))
print(np.zeros((n), dtype=int))
print(np.ones((n), dtype=int))