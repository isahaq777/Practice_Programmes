#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())

    # Checks if the number is odd or if it is even and between 6 and 20, inclusive. 
    is_odd = (n % 2 != 0)
    is_inclusive_range = (6 <= n <= 20)

    # Print "Weird" when 'weird' conditional is True. Otherwise, it sets it to "Not Weird".
    weird_status = "Weird" if (is_odd or is_inclusive_range) else "Not Weird"
    print(weird_status)
