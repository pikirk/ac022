#statements = []
#with open("/Users/pikirk/src/aoc22/day8/1/input.txt", "r") as input:
# statements = input.readlines()

from __future__ import annotations
from typing import Tuple
from enum import Enum
class Corner(Enum):
    NONE = 0
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOT_LEFT = 3
    BOT_RIGHT = 4

class Edge(Enum):
    NONE = 0
    TOP = 1
    RIGHT = 2
    LEFT = 3
    BOT = 4

class Picker:
    def __init__(self):
        self.top = ()
        self.right = ()
        self.bot = ()
        self.left = ()
        self.center = ()
        self.grid_height = 0
        self.grid_width = 0
        self.is_corner = False
        self.edge = Edge.NONE
        self.corner = Corner.NONE
        self.is_edge = False
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
        p.is_corner = True
        p.top_edge_min = (0,1)
        p.top_left_edge_min = (1,0)
        p.top_edge_max = (0, p.grid_width - 2)
        p.top_right_edge_max = (1, p.grid_width - 1)
        p.bottom_edge_max = (p.grid_height -1, p.grid_width - 2)
        p.bottom_right_edge_max = (p.grid_height -2, p.grid_width -1)
        p.bottom_edge_min = (p.grid_height -1, 1)
        p.bottom_left_edge_min = (p.grid_height -2, 0)
        return p

    def visible(self) -> bool:
        print("is visible")
        return False

    @staticmethod
    def shift_right(p:Picker):
        p.top = (p.top[0], p.top[1] + 1)
        p.right = (p.right[0], p.right[1] + 1)
        p.bot = (p.bot[0], p.bot[1] + 1)
        p.left = (p.left[0], p.left[1] + 1)
        p.center = (p.center[0], p.center[1] + 1)
        Picker.setBoundaryState(p)

    @staticmethod
    def start_left(p:Picker):
        p.top = (p.top[0] + 1, p.top[1])
        p.right = (p.right[0] + 1, p.right[1])
        p.bot = (p.bot[0] + 1, p.bot[1])
        p.left = (p.left[0] + 1, p.left[1])
        p.center = (p.center[0] + 1, p.center[1])
        Picker.setBoundaryState(p)

    @staticmethod
    def setBoundaryState(p:Picker):
        p.is_corner = False
        p.is_edge = False
        p.corner = Corner.NONE
        p.edge = Edge.NONE

        # corner states - picker initialized to top left corner
        if ( p.right == p.top_right_edge_max and p.top == p.top_edge_max ):
            p.is_corner = True
            p.corner = Corner.TOP_RIGHT

        elif ( p.right == p.bottom_right_edge_max and p.bot == p.bottom_edge_max ):
            p.is_corner = True
            p.corner = Corner.BOT_RIGHT

        elif ( p.bot == p.bottom_edge_min and p.left == p.bottom_left_edge_min ):
            p.is_corner = True
            p.corner = Corner.BOT_LEFT
        
        elif ( state := p.getEdgeState() == Edge.TOP ):
            p.is_edge = True
            p.edge = state
            
    def preview_shift_right(self):
        edge_test = self.right[1] + 1
        return edge_test <= self.grid_width

    def preview_start_left(self):
        edge_test = self.bot[0] + 1
        return edge_test <= self.grid_height

    def getEdgeState(self): 
        ret_value = Edge.NONE
        print (self.bottom_edge_min)
        print (self.bot)
        print (self.bottom_edge_max)

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
        w = len(len(tree_map[0]))
        self.cur_picker = Picker.init(h, w)
        self.map = tree_map

    def movePicker(self) -> Tuple(int, bool):
        ret_value = ()
        can_shift_right = self.cur_picker.preview_shift_right(len(self.map))
        can_start_left = self.cur_picker.preview_shift_right(len(self.map))
        if can_shift_right:
            Picker.shift_right(self.cur_picker)
            ret_value = (self.cur_picker.center, self.cur_picker.visible())           
        elif can_start_left:
            Picker.start_left(self.cur_picker)
            ret_value = (self.cur_picker.center, self.cur_picker.visible())
        return ret_value

    def getCurrentPicker(self):
        return self.cur_picker

    def getPickerValues(self):
        print('get picker values')

def test_top_edge():
    p = Picker.init(5,5)

     # act
    for r in range(0, 1):
        Picker.shift_right(p)

    # assert
    assert p.getEdgeState() == Edge.TOP


test_top_edge()