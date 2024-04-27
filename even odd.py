#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n%2 != 0:
        print("wierd")
    elif n%2 == 0 and n>2 and n<=5:
        print("Not wierd")
    elif n%2 == 0 and n>6 and n<=20:
        print("wierd")
    else:
        print("Not wierd")            
