#! /usr/bin/python3
import time
with open('day1/input', 'r') as c:
    # Get the data from the file 
    # and split it all into groups
    groups = c.readlines()
for line in groups:
    if line == '\n':
        # Split the lines into groups
        
        # { {total=, ints=[100, 150, 300]}, {total=, ints=[10,65,200]}}


