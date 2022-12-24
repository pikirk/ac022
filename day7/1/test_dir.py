from typing import Tuple
import copy
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
import networkx as nx
from answer import FileSystem

def createDag(statements:list) -> FileSystem:
    fs = FileSystem()

    return fs

def test_deep_tree_filecount():
    # arrange
    statements = ['$ cd /'
    ,'$ ls'
    ,'dir bzgf'
    ,'199775 dngdnvv.qdf'
    ,'dir fhhwv'
    ,'dir gzlpvdhd'
    ,'dir htczftcn'
    ,'23392 lbcgmm'
    ,'251030 lsw.jgr'
    ,'305227 nflgvsgz'
    ,'dir qcqg'
    ,'dir qtqpw'
    ,'dir qzcdscbp'
    ,'dir rfgvg'
    ,'dir rzb'
    ,'202033 zqzlbvgl']

