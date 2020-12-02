import numpy as np


file = open('input.txt', 'r')

lines = file.readlines() 

numValidPart1 = 0
numValidPart2 = 0

for line in lines:
    line = line[:-1]
    line = line.split(':')
    password = line[1][1:]
    policy = line[0]
    
    policy = line[0].split(' ')
    
    letter = policy[1]
    minmax = policy[0].split('-')
    minAmount = int(minmax[0])
    maxAmount = int(minmax[1])
    

    count = password.count(letter)
    
    if count >= minAmount and count <= maxAmount:
        numValidPart1 += 1
        
    if password[minAmount-1] == letter and password[maxAmount-1] != letter:
        numValidPart2 += 1
        
    if password[minAmount-1] != letter and password[maxAmount-1] == letter:
        numValidPart2 += 1
        
    
print("num valid passwords part 1: ", numValidPart1)
print("num valid passwords part 2: ", numValidPart2)