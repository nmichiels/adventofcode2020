import numpy as np
import time
# https://adventofcode.com/2020/day/25

file = open('input.txt', 'r')
lines = file.readlines()

public_keys = [int(key.rstrip()) for key in lines]

def encrypt_subject_number_to_public_key(subject_number, loop_size):
    public_key = 1
    
    for i in range(loop_size):
        public_key = public_key * subject_number
        public_key = public_key % 20201227
        
    return public_key
    
def reverse_engineer_loop_size(target_public_key):
    subject_number = 7
    public_key = 1
    loop_size = 0
    while public_key != target_public_key:
        loop_size+=1
        
        public_key = public_key * subject_number
        public_key = public_key % 20201227
        

    return loop_size
    

print(public_keys)

public_keys_card = public_keys[0]
public_keys_door = public_keys[1]

loop_size_card = reverse_engineer_loop_size(public_keys_card)
loop_size_door = reverse_engineer_loop_size(public_keys_door)

print("Loop sizes: ", loop_size_card, loop_size_door)

encryption_key_door = encrypt_subject_number_to_public_key(public_keys_door, loop_size_card)
encryption_key_card = encrypt_subject_number_to_public_key(public_keys_card, loop_size_door)

print("Encryption keys: ", encryption_key_door, encryption_key_card)