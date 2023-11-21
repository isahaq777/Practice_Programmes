#You are given two integer arrays of size MxP and NxP(M & N are rows,P and is the column). Your task is to concatenate the arrays along axis0.
import numpy as np
N, M, P = list(map(int, input("Enter the space separated integers M,N, and P: ").split()))
arr1 = np.array([input("Enter the N lines contains the space separated elements of the P columns").split() for _ in range(N)], dtype='int')
arr2 = np.array([input("Enter the M lines contains the space separated elements of the P columns").split() for _ in range(M)], dtype='int')
print(np.concatenate((arr1, arr2), axis=0))