import numpy as np

# https://adventofcode.com/2020/day/3

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


def count_trees_for_slope(right, down):
    num_trees = 0
    row = 0
    col = 0
    while row < height:
        if map[row,col] == '#':
            num_trees += 1
            
        row += down
        col += right
        col = col % width
        
    return num_trees
    
    

print("Result part 1, num trees: ", count_trees_for_slope(right=3, down=1))

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
total_trees_multiplied = 1

for slope in slopes:
    total_trees_multiplied = total_trees_multiplied * count_trees_for_slope(right=slope[0], down=slope[1])

print("Result part 2, total trees multiplied: ", total_trees_multiplied)

