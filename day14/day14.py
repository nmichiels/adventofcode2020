import numpy as np
import time
# https://adventofcode.com/2020/day/13



start = time.time()

file = open('input.txt', 'r')
lines = file.readlines()

# data = " ".join([line for line in lines]) 

memory = {}
mask = None
for line in lines:
    if line[0:4] == 'mask':
        mask = line[7:-1]
        mask = np.asarray(list(mask))
    else:
        address = int(line[4:-1].split(']')[0])
        value = int(line[4:-1].split(']')[1][3:])

        # apply binary mask to value
        value_bin = np.asarray(list(format(value, "036b")))
        value_bin[mask != 'X'] = mask[mask != 'X']
        value = int("".join(value_bin.tolist()), 2)
        
        # set memory
        memory[address] = value

print("Result part 1: ", sum(memory.values()))


      

from itertools import product  
memory = {}
mask = None
for line in lines:
    if line[0:4] == 'mask':
        mask = line[7:-1]
        mask = np.asarray(list(mask))
    else:
        address = int(line[4:-1].split(']')[0])
        value = int(line[4:-1].split(']')[1][3:])

        # apply binary mask to value
        address_bin = np.asarray(list(format(address, "036b")))
        address_bin[mask != '0'] = mask[mask != '0']
        
        num_floats = np.count_nonzero(address_bin == 'X')
        permutations = list(map(list, product([0, 1], repeat=num_floats)))
        
        
        for permutation in permutations:
            address_bin_copy = address_bin.copy()
            address_bin_copy[address_bin_copy == 'X'] = permutation
            address = int("".join(address_bin_copy.tolist()), 2)
            memory[address] = value
            



print("Result part 2: ", sum(memory.values()))

end = time.time()
print(end-start)