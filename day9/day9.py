from itertools import combinations 
import numpy as np

data = np.loadtxt('input.txt', delimiter='\n', dtype=np.int64)


# part 1


def find_weakness(data, preamble_length = 25):
    for pos in range(preamble_length, len(data)):
        preamble = data[pos-preamble_length:pos]
        
        all_combinations = np.array(list(combinations(preamble, 2)) )
        all_sums = all_combinations.sum(axis=1)
        
        occurrences = np.count_nonzero(all_sums == data[pos])
        
        if not occurrences:
            return pos
        
        
        
pos = find_weakness(data, 25)
print("Result part 1: ", data[pos])


def find_contiguous_set(data, invalid_number):

    for lbound in range(0,len(data)-1):
        for ubound in range(lbound+1,len(data)):
            set = data[lbound:ubound+1]
            sum = np.sum(set)
            
            
            if sum == invalid_number:
                return set


set = find_contiguous_set(data, data[pos])
print("Result part 2: ", np.min(set) + np.max(set))