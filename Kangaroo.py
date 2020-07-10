#!/bin/python3

import math
import os
import random
import re
import sys

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

if v1 == v2 :
    print('YES' if x1 == x2 else 'NO')
else:
    t = (x1 - x2)/(v2 - v1)
    print('YES' if t.is_integer() and t>=0 else 'NO')
