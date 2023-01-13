from __future__ import annotations
from typing import Tuple

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
Responsible for inspecting the visiblity of tree houses
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
            return self.getPickerValues()           
        
        if can_start_left:
            Picker.start_left(self.cur_picker)

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
    Visibility check for current selected tree
    '''
    def score(self) -> bool:
        cluster = self.getPickerValues()
        tree_house = cluster[2][1]
        tree_house_index = self.cur_picker.center[0]
        heights = self.getX()

        # check view from X edges
        visible_left = self.checkLeftEnd(tree_house, tree_house_index, heights)
        visible_right = self.checkRightEnd(tree_house, tree_house_index, heights)

        if visible_left or visible_right:
            return True

        # check view from Y edges
        heights = self.getY()
        visible_left = self.checkLeftEnd(tree_house, tree_house_index, heights)
        visible_right = self.checkRightEnd(tree_house, tree_house_index, heights)
        
        return visible_left or visible_right

    def checkRightEnd(self, tree_house, tree_house_index, heights):
        visible = False
        for h in range(len(heights) - 1, 0, -1):
            if h == tree_house_index:
                break
            elif heights[h] < tree_house:
                visible = True
            elif heights[h] >= tree_house:
                visible = False
        return visible

    def checkLeftEnd(self, tree_house, tree_house_index, heights) -> bool:
        visible = False
        for h in range(0, len(heights) - 1):
            if h == tree_house_index:
                break
            elif heights[h] < tree_house:
                visible = True
            elif heights[h] >= tree_house:
                visible = False
        return visible

    '''
    Processes grid left to right starting at left corner
    '''
    def scoreGrid(self) -> int:
        ret_value = 0
        # walk inner trees
        while self.cur_picker.preview_shift_right() or self.cur_picker.preview_start_left():
            ret_value +=1 if self.score() else 0
            self.movePicker()

        # perimeter value
        ret_value += (self.cur_picker.grid_width * 2) + ((self.cur_picker.grid_height - 2) * 2)
        return ret_value

    def getY(self) -> list(int):
        result = []
        y = self.cur_picker.top[1]
        for r in range(0, self.cur_picker.grid_height):
            result.append(self.map[r][y])
        return result

    def getX(self) -> list(int):
        result = []
        x = self.cur_picker.left[0]
        for c in range(0, self.cur_picker.grid_height):
            result.append(self.map[x][c])
        return result

rows = []
with open("/Users/pikirk/src/aoc22/day8/1/input.txt", "r") as input:
    for line in input:
        line = line.strip('\n')
        rows.append([int(i) for i in list(line)])

grid = Grid(rows)
print (grid.scoreGrid())
# 7153 too high
# 7037 too high