#!/bin/python3 given an  n integer, , print its first 10 multiples
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    [print(n, 'x', i+1, '=', n*(i+1)) for i in range(10)]
