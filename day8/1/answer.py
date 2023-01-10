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
        self.is_corner = False
        self.is_edge = False
    
    @staticmethod
    def init() -> Picker:
        picker = Picker()
        picker.top = (0,1)
        picker.right = (1,2)
        picker.bot = (2,1)
        picker.left = (1,0)
        picker.center = (1,1)
        picker.is_corner = True
        return picker

    @staticmethod
    def shift_right(p:Picker):
        p.top = (p.top[0], p.top[1] + 1)
        p.right = (p.right[0], p.right[1] + 1)
        p.bot = (p.bot[0], p.bot[1] + 1)
        p.left = (p.left[0], p.left[1] + 1)
        p.center = (p.center[0], p.center[1] + 1)

    @staticmethod
    def start_left(p:Picker):
        print ('start left')

    @staticmethod
    def preview_shift_right(p:Picker, grid_width:int):
        print ('preview shift right')

    @staticmethod
    def preview_start_left(p:Picker, grid_height:int):
        print ('preview start left')

    @staticmethod
    def is_hidden(p:Picker) -> bool:
        return False

class Grid:
    def __init(self, tree_map:list[list[int]]):
        self.cur_picker = Picker.init()
        self.map = tree_map

    def movePicker(self) -> Tuple(int, bool):
        ret_value = ()
        if self.preview_shift_right:
            Picker.shift_right(self.cur_picker)
            ret_value = (self.cur_picker.center, Picker.is_hidden)           
        elif self.preview_start_left:
            Picker.start_left(self.cur_picker)
            ret_value = (self.cur_picker.center, Picker.is_hidden)
        return ret_value

    def getCurrentPicker(self):
        return self.cur_picker
