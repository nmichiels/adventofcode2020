import numpy as np
import time
# https://adventofcode.com/2020/day/16




# data = " ".join([line for line in lines]) 


def load_data():
    file = open('input.txt', 'r')
    lines = file.readlines()
    data = " ".join([line for line in lines]) 

    # data = data.split('your ticket:\n ')
    data = data.split('\n \n ')
    
    # parse classes
    classes_data = data[0].split('\n ')
    classes = {}
    for cls in classes_data:
        cls_data = cls.split(': ')
        cls = cls_data[0]
        ranges_data = cls_data[1].split(' or ')
        
        ranges = []
        for range in ranges_data:
            range_data = range.split('-')
            ranges.append((int(range_data[0]), int(range_data[1])))
           
        classes[cls] = ranges
        
    # parse your ticket
    your_ticket = data[1][14:].split(',')
    your_ticket = [int(t) for t in your_ticket]

    #parse nearby tickets
    nearby_tickets = []
    nearby_data = data[2][17:-1].split('\n ')
    for nearby in nearby_data:
        nearby = nearby.split(',')
        nearby = [int(n) for n in nearby]
        nearby_tickets.append(nearby)
    
    return classes, your_ticket, nearby_tickets

classes, your_ticket, nearby_tickets = load_data()

def is_within_all_class_ranges(number, class_ranges):
    for ranges in class_ranges:
        if is_within_ranges(number, ranges):
            return True
    return False
    
def is_within_ranges(number, ranges):
    for range in ranges:
        if number >= range[0] and number <= range[1]:
            return True
    return False

def get_valid_tickets(nearby_tickets):
    errors = []
    valid_tickets = []
    for ticket in nearby_tickets:
        error = False
        for value in ticket:
            if not is_within_all_class_ranges(value, classes.values()):
                errors.append(value)
                error = True
                
        if not error:
            valid_tickets.append(ticket)
                
    total_error = 0
    for error in errors:
        total_error += error
        
    return total_error, valid_tickets
                

                
total_error, valid_tickets = get_valid_tickets( nearby_tickets)
print("Result part 1: ", total_error)



# find all matching field ids per class
field_ids = np.arange(len(classes))
class_to_field_ids = {}
for cls in classes.keys():
    ranges = classes[cls]
    for i, field_id in enumerate(field_ids):
     
        match = True
        for ticket in valid_tickets:
            if not is_within_ranges(ticket[field_id], ranges):
                match = False
                break
                
        if match is True:
            if cls in class_to_field_ids:
                class_to_field_ids[cls].append(field_id)
            else:
                class_to_field_ids[cls] = [field_id]
            
  


# filter field_ids starting from class with only one matching id
class_to_field_id = {}
while len(class_to_field_ids) > 0:
    # find class with only one id
    identified_class = None 
    id_found = None
    for cls in class_to_field_ids.keys():
        if len(class_to_field_ids[cls]) == 1:
            identified_class = cls
            class_to_field_id[cls] = class_to_field_ids[cls][0]
            id_found = class_to_field_ids[cls][0]
            
    if identified_class:
        del class_to_field_ids[identified_class]
        
        # remove id from other classes
        for cls, ids in class_to_field_ids.items():
            for i, id in enumerate(ids):
                if id == id_found:
                    ids.pop(i)
         
    else:
        print("Error class with one id not found")
           

# fill in fields on ticket
ticket_fields = {}
for cls in classes.keys():
    ticket_fields[cls] = your_ticket[class_to_field_id[cls]]
        
        
# calculate result for part 2
result = 1
for cls, field in ticket_fields.items():
    if cls[0:9] == 'departure':
        result*= field

print("Result part 2: ", result)
    
    
    
    
