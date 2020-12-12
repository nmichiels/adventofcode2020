import numpy as np
import time
# https://adventofcode.com/2020/day/12





file = open('input.txt', 'r')
instructions = file.readlines()
    

degreesToDir = {0:'E', 90:'S', 180:'W', 270:'N'}
position = {'N': 0,'E': 0,'S': 0,'W': 0}


degrees = 0
dir = 'E'

# part 1
for instruction in instructions:
    action = instruction[0]
    units = int(instruction[1:])
    
    
    if action == 'N' or action == 'E' or action == 'S' or action == 'W':
        position[action] += units
        
    if action == 'F':
        position[dir] += units
        
    if action == 'R':
        degrees+=units
        if degrees >=360:
            degrees -= 360
            
        dir = degreesToDir[degrees]
        
    if action == 'L':
        degrees-=units
        if degrees < 0:
            degrees += 360
            
        dir = degreesToDir[degrees]
        
        
   
print("Result part 1: ", abs(position['E']-position['W'])+abs(position['N']-position['S']))



position = {'N': 0,'E': 0,'S': 0,'W': 0}
waypoint = {'N': 1,'E': 10,'S': 0,'W': 0}

dirToIdx = {'N':0, 'E':1, 'S':2, 'W':3}
waypoint = np.array([1, 10, 0, 0])


dirs = ['N','E','S','W']
# part 2
for instruction in instructions:
    action = instruction[0]
    units = int(instruction[1:])
    
    
    if action == 'N' or action == 'E' or action == 'S' or action == 'W':
        waypoint[dirToIdx[action]] += units
        
    if action == 'F':
        position['N'] += units * waypoint[dirToIdx['N']]
        position['E'] += units * waypoint[dirToIdx['E']]
        position['S'] += units * waypoint[dirToIdx['S']]
        position['W'] += units * waypoint[dirToIdx['W']]

        
        
    if action == 'R':
        steps = int(units / 90)
        waypoint = np.roll(waypoint,steps)

        
    if action == 'L':
        steps = int(units / 90)
        waypoint = np.roll(waypoint,-steps)
        
        
   
print("Result part 2: ", abs(position['E']-position['W'])+abs(position['N']-position['S']))
        
            
        
        
    


