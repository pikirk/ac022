from typing import Tuple
import copy
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
import networkx as nx

class FileSystem:
    def __init__(self, statements:list):
        self.dag = nx.DiGraph()
        self.node_counter = 0
        self.cur_node = ()
        self.dag.add_node(self.node_counter, dir='/', files=[])
        self.seen_nodes = [(0, '/')]
        self.parseInput(statements)

    def cd(self, to_node:str):
        if to_node == "..":
            parent = next( iter(self.dag.predecessors(self.cur_node[0])))
            self.cur_node = (parent, self.dag.nodes[parent]['dir'])
        elif to_node == '/':
            self.cur_node = (self.node_counter, '/')
        else:
            for c in iter(self.dag.successors(self.cur_node[0])):
                if self.dag.nodes[c]['dir'] == to_node:
                    self.cur_node = (c, to_node)
                    break

    def mkdir(self, leaf_name:str):
        self.node_counter += 1
        self.dag.add_node(self.node_counter, dir=leaf_name, files=[])
        self.dag.add_edge(self.cur_node[0], self.node_counter)
        self.seen_nodes.append((self.node_counter, leaf_name))

    def addFile(self, file_info:str):
        assert file_info != ''
        file = self.parseFileInfo( file_info )
        self.dag.nodes[self.cur_node[0]]["files"].append( file )

    def parseFileInfo(self, file:str) -> Tuple[int, str]:
        parts = file.split(" ")
        return (int(parts[0]), parts[1])
        check = 100000
        files = self.dag.nodes[0]['files']
        root_size = sum( [f[0] for f in files] )
        return root_size if (root_size <= check) else 0

    def parseInput(self, statements:list):
        ls = []
        for l in range(0, len(statements)):
            statement = statements.pop(0).removesuffix('\n')
            if statement.startswith('$'):
                if statement.startswith('$ cd') and len(ls) == 0:
                    folder = (statement.split(" ")[2])
                    self.cd(folder)

                elif statement.startswith('$ cd') and len(ls) != 0:
                    # create dir or add files to current directory in fs object
                    self.addFiles(ls)

                    # execute cd for current statement
                    folder = (statement.split(" ")[2])
                    self.cd(folder)
            # add ls statements
            else:
                ls.append(statement)
        self.addFiles(ls)

        if len(ls) != 0:
            self.addFiles(ls)

    def addFiles(self, ls:list):
        for s in range(0, len(ls)):
            info = ls.pop(0)
            if info.startswith("dir"):
                dir = info.replace('dir ', '')
                self.mkdir(dir)
            else:
                self.addFile(info)
    
    def getFileCount(self, leaf:int):
        files = self.dag.nodes[leaf]['files']
        return len( [n[0] for n in files] )

    def getDirSize(self, leaf:int):
        files = self.dag.nodes[leaf]['files']
        return sum( [n[0] for n in files] )
        result = list(nx.dfs_postorder_nodes(self.dag))
        return result

    def calculateSize(self) -> int:
        result = 0
        check = 100000
        for n in range(0, len(self.dag.nodes())):
            size = self.calculateDirSize(n)
            if size <= check:
                print (f"{self.dag.nodes[n]['dir'], size}")
                result += size
        return result

    def calculateDirSize(self, node:int) -> int:
        parent_size = 0
        cur_node = node
        files = self.dag.nodes[cur_node]['files']
        parent_size += sum( [f[0] for f in files] )

        children = list(iter(self.dag.successors(cur_node)))
        leaves_size = 0   
        while (len(children) > 0):        
            for c in range(0, len( children )):
                cur_node = children.pop(0)
                files = self.dag.nodes[cur_node]['files']
                leaves_size += sum( [f[0] for f in files] )
                children = children + list(iter(self.dag.successors(cur_node))) 
        return parent_size + leaves_size
            
statements = []
with open("/Users/pikirk/src/aoc22/day7/1/input.txt", "r") as input:
    statements = input.readlines()
fs = FileSystem(statements) 
print (fs.calculateSize() )