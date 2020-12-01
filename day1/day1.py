from itertools import combinations 
import numpy as np

expenses = np.loadtxt('input.txt', delimiter='\n', dtype=np.int)


# part 1

# get all possible combinations of two values
allcombinations = np.array(list(combinations(expenses, 2)) )

# find index of combination with sum == 2020
sum = allcombinations[:,0]+allcombinations[:,1]
index = np.where(sum == 2020)[0]

combination = allcombinations[index].flatten()

print(combination[0], '+', combination[1], "=", combination[0]+combination[1])
print(combination[0], '*', combination[1], "=", combination[0]*combination[1])



# part 2

# get all possible combinations of two values
allcombinations = np.array(list(combinations(expenses, 3)) )

# find index of combination with sum == 2020
sum = allcombinations[:,0]+allcombinations[:,1]+allcombinations[:,2]
index = np.where(sum == 2020)[0]

combination = allcombinations[index].flatten()

print(combination[0], '+', combination[1], '+', combination[2], "=", combination[0]+combination[1]+combination[2])
print(combination[0], '*', combination[1], '*', combination[2], "=", combination[0]*combination[1]*combination[2])
