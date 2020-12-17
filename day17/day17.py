import numpy as np
import time
# https://adventofcode.com/2020/day/17








def get_num_occupied_in_neighborhood(pocket, pos, w_range = 0):
 
    (r, c, z, w) = pos

    num_occupied = 0
    for r_neigbor in range(r-1,r+2):
        for c_neigbor in range(c-1,c+2):
            for z_neigbor in range(z-1,z+2):
                for w_neigbor in range(w-w_range,w+w_range+1):
                    if r_neigbor == r and c_neigbor == c and z_neigbor == z and w_neigbor == w:
                        continue
                        
                    if (str(r_neigbor),str(c_neigbor),str(z_neigbor),str(w_neigbor)) in pocket:
                        num_occupied +=1
            
    return num_occupied
    
    
    
def update(pocket, w_range = 0):
  
    new_pocket = pocket.copy()
    
    for r,c,z,w in pocket.keys():
        r = int(r)
        c = int(c)
        z = int(z)
        w = int(w)
        num_active_neighbors = get_num_occupied_in_neighborhood(pocket, (int(r),int(c),int(z),int(w)),w_range)
        if num_active_neighbors != 2 and num_active_neighbors != 3:
            del new_pocket[str(r),str(c),str(z),str(w)] # becomes inactive
            
        # check neigboring inactive ones
        for r_neigbor in range(r-1,r+2):
            for c_neigbor in range(c-1,c+2):
                for z_neigbor in range(z-1,z+2):
                    for w_neigbor in range(w-w_range,w+w_range+1):
                        if r_neigbor == r and c_neigbor == c and z_neigbor == z and w_neigbor == w:
                            continue
                       
                        # check if neigbor is inactive
                        if (str(r_neigbor),str(c_neigbor),str(z_neigbor),str(w_neigbor)) not in pocket:
                            num_active_neighbors = get_num_occupied_in_neighborhood(pocket, (r_neigbor, c_neigbor, z_neigbor, w_neigbor),w_range)
                            if num_active_neighbors == 3:
                                new_pocket[str(r_neigbor),str(c_neigbor),str(z_neigbor),str(w_neigbor)] = True
                            
    
    return new_pocket
    
    
def load_map(file):
    map = []
    lines = file.readlines()
    for line in lines:
        line = [char for char in line]
        line = line[:-1]
        map.append(line)
    return np.asarray(map)
        

file = open('input.txt', 'r')
map = load_map(file)
[height, width] = map.shape


# create sparse map of active cubes
start_pocket = {}
for r in range(height):
    for c in range(width):
        if map[r,c] == '#':
            start_pocket[str(r),str(c),str(0), str(0)] = True
            
            
# part 1
pocket = start_pocket.copy()
num_cycles = 6
for i in range(num_cycles):
    pocket = update(pocket)
print("Result part 1: ", len(pocket)) 


# part 2
pocket = start_pocket.copy()
num_cycles = 6
for i in range(num_cycles):
    pocket = update(pocket, w_range = 1)
print("Result part 2: ", len(pocket)) 


 