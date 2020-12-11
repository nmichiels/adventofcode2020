import numpy as np

# https://adventofcode.com/2020/day/11

def load_map(file):
    map = []
    lines = file.readlines()
    for line in lines:
        # print(line)
        line = [char for char in line]
        line = line[:-1]
        map.append(line)
    return np.asarray(map)
        



file = open('input.txt', 'r')
map = load_map(file)



[height, width] = map.shape


def get_num_occupied_in_neighborhood_part1(map, pos):
    neighborhood = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    (row,col) = pos

    num_occupied = 0
    for (r,c) in neighborhood:
        if row+r < 0 or row+r >= map.shape[0]:
            continue
        if col+c < 0 or col+c >= map.shape[1]:
            continue
            
        if map[row+r,col+c] == '#':
            num_occupied += 1
            
    return num_occupied
    
    
def get_num_occupied_in_neighborhood_part2(map, pos):
    neighborhood = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    (source_row,source_col) = pos

    num_occupied = 0
    for (r,c) in neighborhood:
        
        border = False
        distance = 1
        while True:
            row = source_row + distance * r 
            col = source_col + distance * c 
        
            if row < 0 or row >= map.shape[0]:
                break
            if col < 0 or col >= map.shape[1]:
                break
            
            if map[row,col] == '#':
                num_occupied += 1
                break
            if map[row,col] == 'L':
                break
                
            distance += 1
            
    return num_occupied
    
    
        
def print_map(map):
    for r in range(map.shape[0]):
        for c in range(map.shape[1]):
            print(map[r,c], end='')
        print('')
    print('')
    
def update_part1(map):
    num_changes = 0
    
    new_map = map.copy()
    
    for r in range(map.shape[0]):
        for c in range(map.shape[1]):
        
            seat = map[r,c]
            
            if seat == 'L' and get_num_occupied_in_neighborhood_part1(map, (r,c)) == 0:
                new_map[r,c] = '#'
                num_changes += 1
                
                
            if seat == '#' and get_num_occupied_in_neighborhood_part1(map, (r,c)) >= 4:
                new_map[r,c] = 'L'
                num_changes += 1
                
    return new_map, num_changes
    
    

def update_part2(map):
    num_changes = 0
    
    new_map = map.copy()
    
    for r in range(map.shape[0]):
        for c in range(map.shape[1]):
        
            seat = map[r,c]
            
            if seat == 'L' and get_num_occupied_in_neighborhood_part2(map, (r,c)) == 0:
                new_map[r,c] = '#'
                num_changes += 1
                
                
            if seat == '#' and get_num_occupied_in_neighborhood_part2(map, (r,c)) >= 5:
                new_map[r,c] = 'L'
                num_changes += 1
                
    return new_map, num_changes
    
print_map(map)

num_changes = 1
while num_changes > 0:
    map, num_changes = update_part1(map)
    
unique, counts = np.unique(map, return_counts=True)
counts = dict(zip(unique, counts))
print("Result part 1:", counts)

     
num_changes = 1
while num_changes > 0:
    map, num_changes = update_part2(map)
    # print_map(map)
    
unique, counts = np.unique(map, return_counts=True)
counts = dict(zip(unique, counts))
print("Result part 2:", counts)
     