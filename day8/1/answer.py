#statements = []
#with open("/Users/pikirk/src/aoc22/day8/1/input.txt", "r") as input:
# statements = input.readlines()

from __future__ import annotations
from typing import Tuple

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
        p.is_corner = False
        p.is_edge = False
            
    def preview_shift_right(self):
        edge_test = self.right[1] + 1
        return edge_test < self.grid_width

    def preview_start_left(self):
        edge_test = self.bot[0] + 1
        return edge_test < self.grid_height

    def getEdgeState(self): 
        ret_value = Edge.NONE

        # top edge
        if self.top > self.top_edge_min and self.top < self.top_edge_max:
            ret_value = Edge.TOP
        # left edge
        elif self.left > self.top_left_edge_min and self.left < self.bottom_left_edge_min:
            ret_value = Edge.LEFT
        # bottom edge
        elif self.bot > self.bottom_edge_min and self.bot < self.bottom_edge_max:
            ret_value = Edge.BOT
            
        return ret_value

class Grid:
    def __init__(self, tree_map:list[list[int]]):
        h = len(tree_map)
        w = len(tree_map[0])
        self.cur_picker = Picker.init(h, w)
        self.map = tree_map

    def movePicker(self) -> Tuple(int, bool):
        ret_value = ()
        can_shift_right = self.cur_picker.preview_shift_right()
        can_start_left = self.cur_picker.preview_start_left()
        if can_shift_right:
            Picker.shift_right(self.cur_picker)
            return self.getPickerValues()           
        
        if can_start_left:
            Picker.start_left(self.cur_picker)
            return self.getPickerValues()
        return ret_value

    def getPickerValues(self) -> list(type()):
        tval = self.map[self.cur_picker.top[0]][self.cur_picker.top[1]]
        t = ('T', tval)

        lval = self.map[self.cur_picker.left[0]][self.cur_picker.left[1]]
        l = ('L', lval)
        
        cval = self.map[self.cur_picker.center[0]][self.cur_picker.center[1]]
        c = ('C', cval)

        rval = self.map[self.cur_picker.right[0]][self.cur_picker.right[1]]
        r = ('R', rval)
        
        bval = self.map[self.cur_picker.bot[0]][self.cur_picker.bot[1]]
        b = ('B', bval)
        
        return (t,l,c,r,b)
    
    def score(self) -> bool:
        cluster = self.getPickerValues()
        top = cluster[0][1]
        left = cluster[1][1]
        tree_house = cluster[2][1]
        right = cluster[3][1]
        bot = cluster[4][1]
        return (top < tree_house or left < tree_house or right < tree_house or bot < tree_house)
