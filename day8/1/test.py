# python3 -m pytest test.py -v --log-cli-level=DEBUG --capture=tee-sys
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
from answer import Grid
from answer import Picker
from  answer import Corner
from answer import Edge

def test_picker_init():
    # arrange
    p = Picker.init(5,5)

    assert p.top == (0,1)
    assert p.right == (1,2)
    assert p.bot == (2,1)
    assert p.left == (1,0)
    assert p.center == (1,1)

def test_shift_right():
    # arrange
    p = Picker.init(5,5)

    # act
    Picker.shift_right(p)

    assert p.top == (0,2)
    assert p.right == (1,3)
    assert p.bot == (2,2)
    assert p.left == (1,1)
    assert p.center == (1,2)

def test_start_left():
    # arrange
    p = Picker.init(5,5)

    # act
    Picker.start_left(p)

    assert p.top == (1,1)
    assert p.right == (2,2)
    assert p.bot == (3,1)
    assert p.left == (2,0)
    assert p.center == (2,1)

def test_start_left_then_shift_right():
    # arrange
    p = Picker.init(5,5)

    # act
    Picker.start_left(p)
    Picker.shift_right(p)

    assert p.top == (1,2)
    assert p.right == (2,3)
    assert p.bot == (3,2)
    assert p.left == (2,1)
    assert p.center == (2,2)

def test_cannot_shift_right():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 3):
        Picker.shift_right(p)

    # act
    result = Picker.preview_shift_right(p)

    assert result == False

def test_last_shift_right():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 2):
        Picker.shift_right(p)

    # act
    result = Picker.preview_shift_right(p)

    assert result == True

def test_cannot_start_left():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 3):
        Picker.start_left(p)

    # act
    result = Picker.preview_start_left(p)

    assert result == False

def test_last_start_left():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 2):
        Picker.start_left(p)

    # act
    result = Picker.preview_start_left(p)

    assert result == True

def test_initial_position_is_top_left():
    # arrange
    p = Picker.init(5,5)

    assert p.is_corner == True

def test_position_is_top_right():
    # arrange
    p = Picker.init(5,5)

    # act
    for c in range(0, 2):
        Picker.shift_right(p)

    assert p.is_corner == True
    assert p.is_edge == False
    assert p.corner == Corner.TOP_RIGHT
    assert p.edge == Edge.NONE

def test_position_is_bottom_right():
    # arrange
    p = Picker.init(5,5)

    # act
    for r in range(0, 2):
        Picker.start_left(p)
    
    for c in range(0, 2):
        Picker.shift_right(p)

    assert p.is_corner == True
    assert p.is_edge == False
    assert p.corner == Corner.BOT_RIGHT
    assert p.edge == Edge.NONE

def test_position_is_bottom_left():
    # arrange
    p = Picker.init(5,5)

     # act
    for r in range(0, 2):
        Picker.start_left(p)

    assert p.is_corner == True
    assert p.is_edge == False
    assert p.corner == Corner.BOT_LEFT
    assert p.edge == Edge.NONE

def test_position_out_of_bounds():
    # arrange
    p = Picker.init(5,5)

     # act
    for r in range(0, 3):
        Picker.start_left(p)

    assert p.is_corner == False

def test_top_edge():
    # arrange
    p = Picker.init(5,5)

     # act
    for r in range(0, 1):
        Picker.shift_right(p)

    assert p.getEdgeState() == Edge.TOP

def test_left_edge():
    # arrange
    p = Picker.init(5,5)

     # act
    for r in range(0, 1):
        Picker.start_left(p)

    assert p.getEdgeState() == Edge.LEFT

def test_bottom_edge():
    # arrange
    p = Picker.init(5,5)

     # act
    for r in range(0, 2):
        Picker.start_left(p)
    for r in range(0, 1):
        Picker.shift_right(p)

    assert p.getEdgeState() == Edge.BOT