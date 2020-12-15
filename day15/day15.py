import numpy as np
import time
# https://adventofcode.com/2020/day/15


input = [0,1,5,10,3,12,19]

memory = {}
numbers = []


def add_memory(number, idx):
    if number in memory.keys():
        memory[number].append(idx)
    else:
        memory[number] = [idx] 
    
# first add all spoken numbers
for i, number in enumerate(input):
    numbers.append(number)
    add_memory(number, i)
    
    
last = numbers[-1]
turn = len(input)
while True:
    if last in memory.keys():
        occurences = memory[last]
        if len(occurences) == 1: #first occurence
            numbers.append(0)
            add_memory(0, turn)
        else:
            new_number = occurences[-1]-occurences[-2]
            numbers.append(new_number)
            add_memory(new_number, turn)
            
         
    if len(numbers) == 30000000:
        break
        
    turn += 1
    last = numbers[-1]
            
print("Result part 1: ", numbers[2019])       
print("Result part 2: ", numbers[-1])
    