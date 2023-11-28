#!/bin/python3 Given an A array, , of N integers, print A's elements in reverse order as a single line of space-separated numbers. 

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])