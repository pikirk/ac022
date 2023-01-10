# python3 -m pytest test_dir.py -v --log-cli-level=DEBUG --capture=tee-sys
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
from answer import Grid
from answer import Picker

def test_picker_init():
    # arrange
    p = Picker.init()

    # assert
    assert p.top == (0,1)
    assert p.right == (1,2)
    assert p.bot == (2,1)
    assert p.left == (1,0)
    assert p.center == (1,1)

def test_shift_right():
    # arrange
    p = Picker.init()

    # act
    Picker.shift_right(p)

    # assert
    assert p.top == (0,2)
    assert p.right == (1,3)
    assert p.bot == (2,2)
    assert p.left == (1,1)
    assert p.center == (1,2)

