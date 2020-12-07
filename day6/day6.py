import numpy as np

# https://adventofcode.com/2020/day/6



def load_groups():
    file = open('input.txt', 'r')
    lines = file.readlines()

    # load groups
    groups = []
    i = 0
    while i < len(lines):
        # get one string for group
        group_str = ''
        while i < len(lines) and lines[i] != '\n':
            group_str = group_str + lines[i]
            i+=1
        group_str = group_str[:-1] # remove last newline
        group_str = group_str.replace("\n", " ")
        
            
        groups.append(group_str)
        

        i+=1
    return groups
        


groups = load_groups()

# part 1
total_anyone  = 0
for group in groups:
    group = group.replace(' ', '')
    group = np.asarray(list(group))   
    total_anyone += len(np.unique(group))
    
print("Result part 1: ", total_anyone)

# part 2
total_everyone = 0
for group in groups:
    group = group.split(' ')
    
    alphabets = []
    for person in group:
        person = np.asarray(list(person))
        alphabet = dict.fromkeys(person, True) #set all unique letters to true in dict
        alphabets.append(alphabet)
    
    # get intersection
    intersection = alphabets[0].keys()
    for i in range(1,len(alphabets)):
        intersection = intersection & alphabets[i].keys()
    
    
    total_everyone += len(intersection)
    
    

print("Result part 2: ", total_everyone)