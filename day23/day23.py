import numpy as np
import time
import re
# https://adventofcode.com/2020/day/23

cups = '215694783'
cups = [int(cup) for cup in list(cups)]

num_cups = len(cups)
num_moves = 100

current_pos = 0
for move in range(num_moves):
    # print("\n move", move+1)
    # print("cups: ", cups)
    current = cups[current_pos]
    
    pickup = [cups.pop(current_pos+1),cups.pop(current_pos+1),cups.pop(current_pos+1)]
    
    destination = current-1
    if destination == 0:
        destination += num_cups
        
    while destination in pickup:
        destination = destination-1
        if destination == 0:
            destination += num_cups
    
    # print("pick up: ", pickup)
    # print("destination: ", destination)
    
    destination_idx = cups.index(destination)
    
    for i in reversed(range(len(pickup))):
        cups.insert(destination_idx+1, pickup[i])
    
    
    current = cups.pop(0)
    cups.append(current)
    
    # current_pos += 1
    # if current_pos == len(cups):
        # current_pos = 0
        
        
print("final cups:", cups)

start_idx = cups.index(1)+1
result = cups[start_idx:] + cups[:start_idx-1]
result = [str(cup) for cup in result]
print("Result part 1: ", ''.join(result))