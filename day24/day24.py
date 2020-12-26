import numpy as np
import time
# https://adventofcode.com/2020/day/24

file = open('input.txt', 'r')
tiles = file.readlines()



dirs_even = {'e' : (0,1), 'se': (1,0), 'sw': (1,-1), 'w': (0,-1), 'nw': (-1,-1), 'ne': (-1,0)}
dirs_odd = {'e' : (0,1), 'se': (1,1), 'sw': (1,0), 'w': (0,-1), 'nw': (-1,0), 'ne': (-1,1)}
floor = {}

reference_tile = np.array([0,0])
for tile in tiles:
    tile = tile.rstrip()
    
    current_tile = reference_tile.copy()
    
    while len(tile) > 0:
        # print(current_tile)
        if current_tile[0] % 2 == 0:
            dirs = dirs_even
        else:
            dirs = dirs_odd
        
        
        if tile[0] == 'e' or tile[0] == 'w':
            current_tile += dirs[tile[0]]
            tile = tile[1:]
            
        else:
            current_tile += dirs[tile[0:2]]
            tile = tile[2:]
            
            
    position_key = str(current_tile[0]) + ',' + str(current_tile[1])
    
    if position_key in floor.keys():
        floor[position_key] = not floor[position_key]
    else:
    
        floor[position_key] = True


def count_black_tiles(floor):
    # count black tiles (True)
    count = 0
    for tile in floor.values():
        if tile == True:
            count += 1
    return count
print("Result part 1: ", count_black_tiles(floor))


def num_adjacent_black_tiles(floor, tile):
    if tile[0] % 2 == 0:
        dirs = dirs_even
    else:
        dirs = dirs_odd
        
    num_black = 0
    for dir in dirs.values():
        neighbor = tile + dir
        
        neighbor_key = str(neighbor[0]) + ',' + str(neighbor[1])
        if neighbor_key in floor.keys() and floor[neighbor_key] == True:
            num_black+=1
            
    return num_black
            

for day in range(100):
    new_floor = floor.copy()
    
    for position, is_black in floor.items():
        tile = np.array([int(position.split(',')[0]), int(position.split(',')[1])])
        
        num = num_adjacent_black_tiles(floor, tile)
        if is_black and (num == 0 or num > 2):
            new_floor[position] = False
            
        if not is_black and num == 2:
            new_floor[position] = True
            
            
        # check all neighboring white ones:
        if is_black:
            if tile[0] % 2 == 0:
                dirs = dirs_even
            else:
                dirs = dirs_odd
                
            for dir in dirs.values():
                neighbor = tile + dir
                neighbor_key = str(neighbor[0]) + ',' + str(neighbor[1])
                if neighbor_key in floor.keys() and floor[neighbor_key] == True:
                    continue
                else:
                    num_neighbor = num_adjacent_black_tiles(floor, neighbor)
                    if num_neighbor == 2:
                        new_floor[neighbor_key] = True
                
            
            
            
    floor = new_floor
        
    
    print("Day", day+1, ":", count_black_tiles(floor))



