
hackerrank



#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the braces function below.
open_list = ["[","{","("] 
close_list = ["]","}",")"]

def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "NO"
    if len(stack) == 0: 
        return "YES"
  

def braces(values):
    result = []
    for val in values:
        result.append(check(val))
    return result


if __name__ == '__main__':