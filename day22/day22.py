import numpy as np
import time
import re
# https://adventofcode.com/2020/day/22

    
    
def load_data():
    file = open('input.txt', 'r')
    lines = file.readlines()
    data = " ".join([line for line in lines]) 
    
    data = data.split('\n \n ')
    
    deck_player1 = data[0][11:].split('\n ')
    deck_player2 = data[1][11:].split('\n ')
    
    deck_player1 = [int(card) for card in deck_player1]
    deck_player2 = [int(card) for card in deck_player2]
    return deck_player1, deck_player2
  

def print_round(round, deck_player1, deck_player2):
    print("-- Round", round, '--')
    print("Player 1's deck:", deck_player1)
    print("Player 2's deck:", deck_player2)
    print('')

def calculate_score(deck_player1, deck_player2):
    if len(deck_player2) > len(deck_player1):
        winning_deck = deck_player2
    else:
        winning_deck = deck_player1
        
    weights = np.array(range(1,len(winning_deck)+1))[::-1]
    score = np.sum(np.asarray(winning_deck) * weights)
    return score

def play_normal_game(deck_player1, deck_player2):

    round = 1
    while True:
        # print_round(round, deck_player1, deck_player2)
        if len(deck_player1) ==0 or len(deck_player2) == 0:
            break
            
            
        card_player1 = deck_player1.pop(0)
        card_player2 = deck_player2.pop(0)
        
        if card_player1 > card_player2:
            deck_player1.append(card_player1)
            deck_player1.append(card_player2)
        else:
            deck_player2.append(card_player2)
            deck_player2.append(card_player1)
        round+=1
        

    if len(deck_player2) > len(deck_player1):
        winning_deck = deck_player2
    else:
        winning_deck = deck_player1
        
    weights = np.array(range(1,len(winning_deck)+1))[::-1]

    score = np.sum(np.asarray(winning_deck) * weights)
    # print("Player 1's deck:", deck_player1)
    # print("Player 2's deck:", deck_player2)
    return deck_player1, deck_player2
    
deck_player1, deck_player2 = load_data()

result_deck_player1, result_deck_player2 = play_normal_game(deck_player1.copy(), deck_player2.copy())
print("Result Part 1: score: ", calculate_score(result_deck_player1, result_deck_player2))




def play_recursive_combat(deck_player1, deck_player2):
    winner_game = 0
    previous_rounds = {}
    round = 1
    while True:
        winner_round = -1
        # print_round(round, deck_player1, deck_player2)
        if len(deck_player1) == 0:
            winner_game = 2
            break
        if len(deck_player2) == 0:
            winner_game = 1
            break
            
            
        hash = ','.join(str(x) for x in deck_player1) + '/' + ','.join(str(x) for x in deck_player2)
        # print(hash)
        if hash in previous_rounds.keys():
            winner_game = 1
            break
        previous_rounds[hash] = round
        
        
        card_player1 = deck_player1.pop(0)
        card_player2 = deck_player2.pop(0)
        

        if card_player1 <= len(deck_player1) and card_player2 <= len(deck_player2):
            # recursive combat
            winner_round, _, _ = play_recursive_combat(deck_player1[:card_player1], deck_player2[:card_player2])
        else:
            if card_player1 > card_player2:
                winner_round = 1
            else:
                winner_round = 2
            
            
        if winner_round == 1:
            deck_player1.append(card_player1)
            deck_player1.append(card_player2)
        elif winner_round == 2:
            deck_player2.append(card_player2)
            deck_player2.append(card_player1)
        else:
            print("Error no winner round")
         
            
        
        round += 1
        
    return winner_game,deck_player1, deck_player2
       

winner_game,result_deck_player1, result_deck_player2 = play_recursive_combat(deck_player1.copy(), deck_player2.copy())
print("Result Part 2: score: ", calculate_score(result_deck_player1, result_deck_player2))
