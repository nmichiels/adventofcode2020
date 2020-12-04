import numpy as np
import re

# https://adventofcode.com/2020/day/4




file = open('input.txt', 'r')
lines = file.readlines()


i = 0

# make list of passports dictionaries
passports = []
while i < len(lines):
    # get one string for passport
    passport_str = ''
    while i < len(lines) and lines[i] != '\n':
        passport_str = passport_str + lines[i]
        i+=1
    passport_str = passport_str[:-1] # remove last newline
    passport_str = passport_str.replace("\n", " ")
    
    # create dictionary of passport content
    passport = {}
    passport_fields = passport_str.split(' ')
    for passport_field in passport_fields:
        field = passport_field.split(':')
        passport[field[0]] = field[1]
        
    passports.append(passport)
    

    i+=1


def check_passport(passport):
    
    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False

    
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    
    hgt = passport['hgt']
    if hgt[-1] is not 'm' and hgt[-1] is not 'n':
        return False
    

    hgt_format = hgt[-2:]
    hgt = int(hgt[:-2])
    
    if hgt_format=='cm' and (hgt < 150 or hgt > 193):
        return False
    if hgt_format=='in' and (hgt < 59 or hgt > 76):
        return False
        
    hcl = passport['hcl']
    hcl = re.findall(r'^#[0-9a-f]{6}$', hcl)
    if len(hcl) == 0:
        return False

    
    
    ecl = passport['ecl']
    if not(ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
        return False

    pid = passport['pid']
    pid = re.findall(r'^[0-9]{9}$', pid)
    if len(pid) == 0:
        return False
    print(passport['pid'])  
        
    return True
    

# part 1 get number of valid passports (ignoring cid)
required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
num_valid_part_1 = 0
num_valid_part_2 = 0
for passport in passports:
    error = False
    for field in required_fields:
        if field not in passport:
            error = True
            break
            
    if not error:
        
        num_valid_part_1 += 1
        if check_passport(passport): # apply additional check for part 2
            num_valid_part_2 += 1
        
        
print("Valid passports part 1: ", num_valid_part_1)
print("Valid passports part 2: ", num_valid_part_2)
