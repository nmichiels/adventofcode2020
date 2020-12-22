import numpy as np
import time
import re
# https://adventofcode.com/2020/day/20

TILE_SIZE = 10

def show_tile(tile):
    for r in range(TILE_SIZE):
        for c in range(TILE_SIZE):
            print(tile[r,c], end='')
        print('')


def show_full_img(img, tiles):
    for row in range(img.shape[0]):
        for r in range(TILE_SIZE):
            for col in range(img.shape[1]):
                for c in range(TILE_SIZE):
                    if img[row,col] == -1:
                        tile = np.ones((TILE_SIZE,TILE_SIZE))*-1
                    else:
                        tile = tiles[img[row,col]]
                        
                    if tile[r,c] == 0:
                        print('.', end='')
                    elif tile[r,c] == 1:
                        print('#', end='')
                    else:
                        print(' ', end='')
                print('  ', end='')
            print('')
        print('\b')
        
        
def show_single_tile(tile):
    for r in range(TILE_SIZE):
        for c in range(TILE_SIZE):
            if tile[r,c] == 0:
                print('.', end='')
            elif tile[r,c] == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print('')
        
def show_img(img_ids, tiles):
    hstacks = []
    for row in range(img_ids.shape[0]):
        htiles = [tiles[i] for i in img_ids[row]]
        hstacks.append(np.hstack(htiles))
        

        
    img = np.vstack(hstacks)
    print(img) 
        
    # tile = np.ones((3,3), dtype=np.int)
    
    # test = [[tile, tile],[tile,tile]]
    
    # test = np.concatenate(test)
    # print(test.shape)
    
    
def load_data():
    file = open('input.txt', 'r')
    lines = file.readlines()
    data = " ".join([line for line in lines]) 

    # data = data.split('your ticket:\n ')
    data = data.split('\n \n ')
    
    tile_ids = []
    tiles = {}
    for tile_data in data:
        
        
        tile_data = tile_data.split('\n ')
        
        tile_id = int(tile_data[0][5:-1])
        tile_ids.append(tile_id)
        
        tile = np.zeros((TILE_SIZE,TILE_SIZE), dtype=np.uint8)
        
        # build tiles
        for row, tile_row in enumerate(tile_data[1:]):
            for col in range(TILE_SIZE):
                if tile_row[col] == '#':
                    tile[row,col] = 1
        tiles[tile_id] = tile
       
    return tile_ids, tiles



def check_valid_tile_pos(pos, tile, img, tiles):
    # check top
    if pos[0]-1 >= 0 and img[pos[0]-1,pos[1]] >= 0:
        top_tile = tiles[img[pos[0]-1,pos[1]]]
        
        if not (top_tile[-1,:] == tile[0,:]).all():
            return False
            
    # check bottom
    if pos[0]+1 < img.shape[0] and img[pos[0]+1,pos[1]] >= 0:
        bottom_tile = tiles[img[pos[0]+1,pos[1]]]
        
        if not (bottom_tile[0,:] == tile[-1,:]).all():
            return False
            
            
    # check left
    if pos[1]-1 >= 0 and img[pos[0],pos[1]-1] >= 0:
        left_tile = tiles[img[pos[0],pos[1]-1]]
        
        if not (left_tile[:,-1] == tile[:,0]).all():
            return False
            
    # check right
    if pos[1]+1 < img.shape[1] and img[pos[0],pos[1]+1] >= 0:
        right_tile = tiles[img[pos[0],pos[1]+1]]
        
        if not (right_tile[:,0] == tile[:,-1]).all():
            return False

    
    return True
    
def find_layout(positions_left,tiles_left, tiles, img):

    if len(positions_left) == 0:
        print("Found result")
        return img, tiles
        
    
    # if len(positions_left) == 143:
        # show_full_img(img, tiles)   
    pos = positions_left[0]
    for i, tile_id in enumerate(tiles_left):
        tile = tiles[tile_id]
        
        
                # 
                # print(tiles_left)
            # import sys
            # sys.exit(0)
        
        for flip in range(2):
            if flip == 0:
                tile_flipped = tile
            elif flip == 1:
                tile_flipped = np.flipud(tile)
            # elif flip == 2:
                # tile_flipped = np.fliplr(tile)
            # elif flip == 3:
                # tile_flipped = np.flipud(np.fliplr(tile))
                
                
            for rot in range(4):
                tile_rot = np.rot90(tile_flipped, k=rot)
                
                # if tile_id == 3079:# and tiles_left[0] == 3079:
                    # print(img)
                    # for rot in range(4):
                        # img[pos[0],pos[1]] = 3079
                        # tiles[tile_id] = tile_rot
                        # show_full_img(img, tiles)
                        
                
                # if img[0,0] == 1951 and img[0,1] == 2311 and pos[0] == 0 and pos[1] == 1 and tile_id == 3079:
                    # print(tiles[img[0,1]][:,-1], "==", tile_rot[:,0])
                    # print(tiles[img[0,1]][:,-1] == tile_rot[:,0])
                if check_valid_tile_pos(pos, tile_rot, img, tiles):
                    
                    img = img.copy()
                    
                    img[pos[0],pos[1]] = tile_id
                    
                    
                    # go deeper
                    # remove element
                    tiles_left.pop(i) # remove this tile from list
                    tiles[tile_id] = tile_rot
                        
                    result, _ = find_layout(positions_left[1:],tiles_left, tiles, img)
                    
                    
                    if result is not None:
                        return result, tiles #result found
                        
                    # reset state by re-inserting element
                    tiles_left.insert(i, tile_id)
                    tiles[tile_id] = tile
                else:
                    # not valid, skip this tile
                    continue
            
    return None, tiles
    

tile_ids, tiles = load_data()

img_size = int(np.sqrt(len(tile_ids)))
print(img_size)


from itertools import product
positions_left = list(product(np.arange(img_size), repeat=2)) 




print(positions_left)

# show_single_tile(tiles[3079])




img_ids = np.ones((img_size,img_size), dtype=np.int) * -1



# img_ids[0,0] = 1951
# img_ids[0,1] = 2311


img, _ = find_layout(positions_left, tile_ids, tiles, img_ids)
print(img)
print("Result part 1: ", img[0,0], '*', img[-1,0], '*', img[0,-1], '*', img[-1,-1])
print("Result part 1: ", np.int64(img[0,0])*img[-1,0]*img[0,-1]*img[-1,-1])



def build_img(input_img, tiles):
    img = np.zeros((input_img.shape[0] * (TILE_SIZE - 2),input_img.shape[1] * (TILE_SIZE - 2)), dtype=np.uint8)
    tile_size = TILE_SIZE-2
    for r in range(input_img.shape[0]):
        for c in range(input_img.shape[1]):
            img[r*tile_size:r*tile_size+tile_size,c*tile_size:c*tile_size+tile_size] = tiles[input_img[r,c]][1:-1,1:-1]
    
    print(img.shape)
    
    return img
    

show_full_img(img, tiles)


def print_img(img):
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            if img[r,c] == 1:
                print('#', end='')
            elif img[r,c] == 2:
                print('O', end='')
            else:
                print('.', end='')
        print('')
    print('')
    

# part 2
import skimage

img = build_img(img, tiles)
print_img(img)

monster = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]], dtype=np.uint8)



sea = img.copy()

for flip in range(2):
    if flip == 0:
        monster_flipped = monster
    elif flip == 1:
        monster_flipped = np.flipud(monster)
        
    for rot in range(4):
        monster_rot = np.rot90(monster_flipped, k=rot)
        mask = monster_rot > 0
        
        windows = skimage.util.view_as_windows(img, mask.shape)

        for r in range(windows.shape[0]):
            for c in range(windows.shape[1]):
               loc = np.where(np.all(windows[r,c,:,:][mask] == monster_rot[mask], axis = -1))[0]
               
               if len(loc) > 0:
                sea[r:r+monster_rot.shape[0],c:c+monster_rot.shape[1]][mask] = 2


print_img(sea)
unique, counts = np.unique(sea, return_counts=True)
counts = dict(zip(unique, counts))
print("Result part 2: ", counts[1])