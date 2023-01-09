
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
from answer import FileSystem

# python3 -m pytest test_dir.py -v --log-cli-level=DEBUG --capture=tee-sys
def test_sample_input():
    # arrange
    statements = [
    '$ cd /'
    ,'$ ls'
    ,'dir a'
    ,'14848514 b.txt'
    ,'8504156 c.dat'
    ,'dir d'
    ,'$ cd a'
    ,'$ ls'
    ,'dir e'
    ,'29116 f'
    ,'2557 g'
    ,'62596 h.lst'
    ,'$ cd e'
    ,'$ ls'
    ,'584 i'
    ,'$ cd ..'
    ,'$ cd ..'
    ,'$ cd d'
    ,'$ ls'
    ,'4060174 j'
    ,'8033020 d.log'
    ,'5626152 d.ext'
    ,'7214296 k'
    ]

    # act
    fs = FileSystem(statements)

    # assert
    assert (fs.getFileCount(0) == 2)
    assert (fs.getDirSize(0) == 14848514 + 8504156)
    assert (fs.getFileCount(1) == 3)
    assert (fs.getDirSize(1) == 29116 + 2557 + 62596)
    assert (fs.getFileCount(3) == 1)
    assert (fs.getDirSize(3) == 584)
    assert (fs.getFileCount(2) == 4)
    assert (fs.getDirSize(2) == 4060174 + 8033020 + 5626152 + 7214296)
    assert (fs.calculateSize() == 95437)

def test_deep_calc():
    # arrange
    #        root
    #         |
    #         a
    #       /   \
    #      b     e
    #     / \   / \
    #    c   d  f  g 
    statements = [
    '$ cd /'
    ,'$ ls'
    ,'dir a'
    ,'100 r.txt'
    ,'100 r.dat'
    ,'100 r.lst'
    ,'$ cd a'
    ,'$ ls'
    ,'200 a.txt'
    ,'200 a.dat'
    ,'200 a.lst'
    ,'dir b'
    ,'dir e'
    ,'$ cd b'
    ,'$ ls'
    ,'dir c'
    ,'dir d'
    ,'300 b.txt'
    ,'300 b.dat'
    ,'300 b.lst'
    ,'$ cd c'
    ,'$ ls'
    ,'400 c.txt'
    ,'400 c.dat'
    ,'400 c.lst'
    ,'$ cd ..'
    ,'$ cd d'
    ,'$ ls'
    ,'500 d.txt'
    ,'500 d.dat'
    ,'500 d.lst'
    ,'$ cd ..'
    ,'$ cd ..'
    ,'$ cd e'
    ,'$ ls'
    ,'600 e.txt'
    ,'600 e.dat'
    ,'600 e.lst'
    ,'dir f'
    ,'$ cd f'
    ,'700 f.txt'
    ,'700 f.dat'
    ,'700 f.lst'
    ]

    # act
    fs = FileSystem(statements)
    result = fs.calculateSize()

    # assert
    assert result == 28800