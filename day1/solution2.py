#! /usr/bin/python3
import time
with open('day1/input', 'r') as c:
    # Get the data from the file 
    # and split it all into groups
    groups = c.read().split('\n')
biggest = 0
notwo = 0
nothree = 0 
count = 0
# Keep adding numbers till you hit an empty line
for num in groups:
    if num != '':
        print(f"{num} + {count} = {int(num) + count}")
        count = int(num) + count
    else:
    # Compare the current group to previous largest number
        if count > biggest:
            print(f"New largest.\nWas: {biggest}\nIs now:{count}")
            biggest = count
        
        else: print(f"Not larger.\nLargest: {biggest}\nCurrent group: {count}")
        # Reset to 0 for next group
        count = 0
# Print the largest number we found
print(f"largest number: {biggest}")





# 165166743
# 165166743