from __future__ import annotations
from typing import Tuple
import numpy as np
import math

'''
Responsible for knowing its position on the tree map
'''
class Picker:
    def __init__(self):
        self.top = ()
        self.right = ()
        self.bot = ()
        self.left = ()
        self.center = ()
        self.grid_height = 0
        self.grid_width = 0
        self.top_edge_min = ()
        self.top_left_edge_min = ()
        self.top_edge_max = ()
        self.top_right_edge_max = ()
        self.bottom_edge_max = ()
        self.bottom_right_edge_max = ()
        self.bottom_edge_min = ()
        self.bottom_left_edge_min = ()
    
    @staticmethod
    def init(grid_height:int, grid_width:int) -> Picker:
        p = Picker()
        p.top = (0,1)
        p.right = (1,2)
        p.bot = (2,1)
        p.left = (1,0)
        p.center = (1,1)
        p.grid_height = grid_height
        p.grid_width = grid_width
        p.top_edge_min = (0,1)
        p.top_left_edge_min = (1,0)
        p.top_edge_max = (0, p.grid_width - 2)
        p.top_right_edge_max = (1, p.grid_width - 1)
        p.bottom_edge_max = (p.grid_height -1, p.grid_width - 2)
        p.bottom_right_edge_max = (p.grid_height -2, p.grid_width -1)
        p.bottom_edge_min = (p.grid_height -1, 1)
        p.bottom_left_edge_min = (p.grid_height -2, 0)
        return p

    @staticmethod
    def shift_right(p:Picker):
        p.top = (p.top[0], p.top[1] + 1)
        p.right = (p.right[0], p.right[1] + 1)
        p.bot = (p.bot[0], p.bot[1] + 1)
        p.left = (p.left[0], p.left[1] + 1)
        p.center = (p.center[0], p.center[1] + 1)

    @staticmethod
    def start_left(p:Picker):
        p.top = (p.top[0] + 1, 1) 
        p.right = (p.right[0] + 1, 2) 
        p.bot = (p.bot[0] + 1, 1) 
        p.left = (p.left[0] + 1, 0) 
        p.center = (p.center[0] + 1, 1) 
            
    def preview_shift_right(self):
        edge_test = self.right[1] + 1
        return edge_test < self.grid_width

    def preview_start_left(self):
        edge_test = self.bot[0] + 1
        return edge_test < self.grid_height

'''
Responsible for inspecting the scenic view of tree houses
'''
class Grid:
    def __init__(self, tree_map:list[list[int]]):
        h = len(tree_map)
        w = len(tree_map[0])
        self.cur_picker = Picker.init(h, w)
        self.map = tree_map

    def movePicker(self):
        can_shift_right = self.cur_picker.preview_shift_right()
        can_start_left = self.cur_picker.preview_start_left()
        if can_shift_right:
            Picker.shift_right(self.cur_picker)            
        elif can_start_left:
            Picker.start_left(self.cur_picker)
        else:
            print("Picker did not move")

    '''
    Looks up grid values based on the picker's current position
    '''
    def getPickerValues(self) -> list(type()):
        # top
        tval = self.map[self.cur_picker.top[0]][self.cur_picker.top[1]]
        t = ('T', tval)
        # left
        lval = self.map[self.cur_picker.left[0]][self.cur_picker.left[1]]
        l = ('L', lval)
        # center
        cval = self.map[self.cur_picker.center[0]][self.cur_picker.center[1]]
        c = ('C', cval)
        # right
        rval = self.map[self.cur_picker.right[0]][self.cur_picker.right[1]]
        r = ('R', rval)
        # bottom
        bval = self.map[self.cur_picker.bot[0]][self.cur_picker.bot[1]]
        b = ('B', bval)
        
        return (t,l,c,r,b)
    
    '''
    Scenic view check for current selected tree
    '''
    def score(self) -> int:
        cluster = self.getPickerValues()
        tree_house = cluster[2][1]
        tree_house_index_x = self.cur_picker.center[1]
        tree_house_index_y = self.cur_picker.center[0]
        x = self.getX()
        y = self.getY()
        view = self.getScenicView(tree_house, tree_house_index_y, tree_house_index_x, x,y)
        return math.prod(view)

    def getScenicView(self, tree_house:int, tree_house_index_y:int, tree_house_index_x:int, x:list[int], y:list[int]) ->list[int]:
        view_count = []
        seen_count = 0
        # up
        for h in range(tree_house_index_y - 1, -1, -1):
            if y[h] < tree_house:
                seen_count +=1
            elif y[h] >= tree_house:
                seen_count +=1
                break
        if ( seen_count > 0 ):
            view_count.append(seen_count)
        
        # down
        seen_count = 0
        for h in range(tree_house_index_y + 1, len(y)):
            if y[h] < tree_house:
                seen_count +=1
            elif y[h] >= tree_house:
                seen_count +=1
                break
        if ( seen_count > 0 ):
            view_count.append(seen_count)
            
        # left
        seen_count = 0
        for h in range(tree_house_index_x -1, -1, -1):
            if x[h] < tree_house:
                seen_count +=1
            elif x[h] >= tree_house:
                seen_count +=1
                break
        if ( seen_count > 0 ):
            view_count.append(seen_count)

        # right
        seen_count = 0
        for h in range(tree_house_index_x + 1, len(x)):
            if x[h] < tree_house:
                seen_count +=1
            elif x[h] >= tree_house:
                seen_count +=1
                break
        if ( seen_count > 0 ):
            view_count.append(seen_count)

        return view_count;

    '''
    Processes grid left to right starting at left corner
    '''
    def scoreGrid(self) -> int:
        high_score = 0
        seen_score = 0

        # first inner scene score - picker initialized at left top corner
        high_score += self.score()
        while self.cur_picker.preview_shift_right() or self.cur_picker.preview_start_left():
            self.movePicker()
            seen_score = self.score()
            high_score = seen_score if seen_score > high_score else high_score
        return high_score

    def getY(self) -> list(int):
        result = []
        y = self.cur_picker.top[1]
        for r in range(0, self.cur_picker.grid_height):
            result.append(self.map[r][y])
        return result

    def getX(self) -> list(int):
        result = []
        x = self.cur_picker.left[0]
        for c in range(0, self.cur_picker.grid_width):
            result.append(self.map[x][c])
        return result

map = []
with open("/Users/pikirk/src/aoc22/day8/2/input.txt", "r") as input:
    for line in input:
        map.append([int(i) for i in list(line.strip('\n'))])

grid = Grid(map)
print (grid.scoreGrid())

def test_middle_row_right_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    for r in range (1, 8):
        grid.movePicker()

    assert 8 == grid.score()


