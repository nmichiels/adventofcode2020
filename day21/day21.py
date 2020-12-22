import numpy as np
import time
import re
# https://adventofcode.com/2020/day/21

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
    
    
def load_data():
    file = open('input.txt', 'r')
    lines = file.readlines()
    allergenToFood = {}
    
    food = {}
    for i, line in enumerate(lines):
        line = line.rstrip()
        
        allergens = line[line.find('(')+10:-1].split(', ')
        ingredients = line[0:line.find('(')-1].split(' ')
        
        
        food[i] = (allergens, ingredients)
        
        # for ingredient in ingredients:
            # if ingredient in ingredientsToAllergies.keys():
                # ingredientsToAllergies[ingredient] = intersection(ingredientsToAllergies[ingredient],allergens)
            # else:
                # ingredientsToAllergies[ingredient] = allergens
        
        # print(ingredientsToAllergies)
        
        
        for allergen in allergens:
            if allergen in allergenToFood.keys():
                allergenToFood[allergen] = intersection(allergenToFood[allergen],ingredients)
                
                
                #allergenToFood[allergen].append(ingredients)
            else:
                allergenToFood[allergen] = ingredients
                

    # filter out doubles
    filtered = {}
    while len(allergenToFood) > 0:
        identified_allergen = None 
        for allergen in allergenToFood.keys():
            if len(allergenToFood[allergen]) == 1:
                identified_allergen = allergen
                break
        
        if identified_allergen:
            
            ingredient_found = allergenToFood[identified_allergen][0]
            filtered[identified_allergen] = ingredient_found
            # print(identified_allergen, ingredient_found)
            del allergenToFood[identified_allergen]
            
            # remove id from other classes
            for allergen, ingredients in allergenToFood.items():
                for i, ingredient in enumerate(ingredients):
                    if ingredient == ingredient_found:
                        ingredients.pop(i)
             
        else:
            print("Error allergen with one id not found")
                
    print(filtered)
        
    count = 0
    for ingredients, allergens in food.values():
        for allergen in allergens:
            if not allergen in filtered.values():
                count += 1
                
    print("Result part 1: ", count)
    
    sort_filtered = sorted(filtered.items(), key=lambda x: x[0])
    
    canonical_dangerous_ingredients_list = [ingredient for (allergen,ingredient) in sort_filtered]
    print(",".join(canonical_dangerous_ingredients_list))
  

            
load_data()
