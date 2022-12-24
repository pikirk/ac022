from typing import Tuple
import copy
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
from answer import FileSystem

def test_shallow_tree_filestats():
    # arrange
    statements = ['$ cd /\n'
    ,'$ ls\n'
    ,'dir A\n'
    ,'199775 R1.txt\n'
    ,'dir B\n'
    ,'dir C\n'
    ,'dir D\n'
    ,'23392 R2.txt\n'
    ,'251030 R3.txt\n'
    ,'305227 R4.txt\n'
    ,'dir E\n'
    ,'dir F\n'
    ,'dir G\n'
    ,'dir H\n'
    ,'dir I\n'
    ,'202033 R5.txt\n'
    ,'dir Z\n']

    # act
    fs = FileSystem(statements)

    # assert
    assert (fs.getFileCount('/') == 5)
    assert (fs.getDirSize('/') == 199775 + 23392 + 251030 + 305227 + 202033)
    assert (fs.getFileCount('A') == 0)
    assert (fs.getDirSize('A') == 0)
    assert (fs.getFileCount('D') == 0)
    assert (fs.getDirSize('D') == 0)
    assert (fs.getFileCount('H') == 0)
    assert (fs.getDirSize('H') == 0)
    assert (fs.getFileCount('I') == 0)
    assert (fs.getDirSize('I') == 0)

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
    assert (fs.getFileCount('/') == 2)
    assert (fs.getDirSize('/') == 14848514 + 8504156)
    assert (fs.getFileCount('a') == 3)
    assert (fs.getDirSize('a') == 29116 + 2557 + 62596)
    assert (fs.getFileCount('e') == 1)
    assert (fs.getDirSize('e') == 584)
    assert (fs.getFileCount('d') == 4)
    assert (fs.getDirSize('d') == 4060174 + 8033020 + 5626152 + 7214296)

