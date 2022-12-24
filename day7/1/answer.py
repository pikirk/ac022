from typing import Tuple
import copy
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
import networkx as nx

class FileSystem:
    def __init__(self):
        self.dag = nx.DiGraph()
        self.dag.add_nodes_from([("/", {"files" : [] } )])
        self.cur_node = "/"
        self.seen_nodes = [self.cur_node]

    def cd(self, to_node:str):
        assert self.seen_nodes.count(to_node) == 1 or to_node == '..'
        if to_node == "..":
            for parent in  iter(self.dag.predecessors(self.cur_node)):
                self.cur_node = parent
        else:
            self.cur_node = to_node

    def mkdir(self, leaf_name:str):
        if self.seen_nodes.count(leaf_name) == 0:
            self.dag.add_nodes_from([(leaf_name, {"files" : [] } )])
            self.dag.add_edge(self.cur_node, leaf_name)
            self.seen_nodes.append(leaf_name)

    def addFile(self, file_info:str):
        assert file_info != ''
        file = self.parseFileInfo( file_info )
        self.dag.nodes[self.cur_node]["files"].append( file )

    def parseFileInfo(self, file:str) -> Tuple[int, str]:
        parts = file.split(" ")
        return (int(parts[0]), parts[1])

    def calculateSize(self) -> int:
        roots = (v for v, d in self.dag.in_degree() if d == 0)
        leaves = [v for v, d in self.dag.out_degree() if d == 0]
        all_paths = []
        for root in roots:
            paths = nx.all_simple_paths(self.dag, root, leaves)
            all_paths.extend(paths)
        
        sum = 0
        for p in range(0, len(all_paths)):
            result = self.getSize( all_paths.pop() )
            if result <= 100000: sum+=result
        return sum

    def getSize2(self, path:list) -> int:
        nodes = path.copy()
        result = 0
        check = 100000
        while len(nodes) != 0:
            dir_size = 0
            for n in range(0, len(nodes)):
                node = nodes[n]
                files = self.dag.nodes[node]['files']
                dir_size += sum( [n[0] for n in files] )
            
            if dir_size <= check:
                result += dir_size
            
            nodes.pop(0)
        return result 

    def getSize(self, path:list) -> int:
        nodes = copy.deepcopy(path)
        nodes.pop(0) # handle root later
        check = 100000
        dir_size = 0
        for n in range(0, len(nodes)):
            node = nodes[n]
            files = self.dag.nodes[node]['files']
            dir_size += sum( [n[0] for n in files] )

        if dir_size > check:
            dir_size = 0

        # sum the last leaf
        dir_last = 0
        if dir_size != 0:
            nodes = copy.deepcopy(path)
            nodes.remove('/')
            if (len(nodes) > 1):
                last = nodes.pop(-1)
                files = self.dag.nodes[last]['files']
                dir_last = sum( [n[0] for n in files] )

        return dir_size + dir_last
    
    def getRootSize(self) -> int:
        check = 100000
        files = self.dag.nodes['/']['files']
        root_size = sum( [n[0] for n in files] )
        return root_size if (root_size <= check) else 0

    def printDirSizes(self):
        roots = (v for v, d in self.dag.in_degree() if d == 0)
        leaves = [v for v, d in self.dag.out_degree() if d == 0]
        all_paths = []
        for root in roots:
            paths = nx.all_simple_paths(self.dag, root, leaves)
            all_paths.extend(paths)

        total = 0
        paths = copy.deepcopy(all_paths)

        for p in range (0, len(paths)):
            path = paths[p]
            dir_size = 0
            path.remove('/')
            for n in range(0, len(path)):
                node = path[n]
                files = self.dag.nodes[node]['files']
                dir_size += sum( [n[0] for n in files] ) 

            mark = "---->" if (dir_size <= 100000) else ""   
            print (f"{mark}{all_paths[p]}={dir_size}")
            total += dir_size

        paths = copy.deepcopy(all_paths)
        for n in range(0, len(paths)):
            path = paths[n]
            path.remove('/')
            if (len(path) > 1):
                node = path.pop(-1)
                files = self.dag.nodes[node]['files']
                size = sum( [n[0] for n in files] ) 
                mark = "---->" if (size <= 100000) else ""   
                print (f"{mark}Dir:{node}={size}")

lines = []
with open("/Users/pikirk/src/aoc22/day7/1/input.txt", "r") as input:
    lines = input.readlines()

fs = FileSystem()
statements = []
ls = []
statement = ''
cd_counter = 0
ls_counter = 0
dir_counter = 0
file_counter = 0

def addFiles(fs, ls):
    global dir_counter 
    global file_counter
    for s in range(0, len(ls)):
        info = ls.pop(0)
        if info.startswith("dir"):
            dir = info.replace('dir ', '')
            fs.mkdir(dir)
            dir_counter += 1
        else:
            file_counter += 1
            fs.addFile(info)

for l in range(0, len(lines)):
    statement = lines.pop(0).removesuffix('\n')
    if statement.startswith('$'):
        if statement.startswith('$ cd') and len(ls) == 0:
            folder = (statement.split(" ")[2])
            fs.cd(folder)
            cd_counter += 1

        elif statement.startswith('$ cd') and len(ls) != 0:
            # create dir or add files to current directory in fs object
            ls_counter += 1
            addFiles(fs, ls)

            # execute cd for current statement
            folder = (statement.split(" ")[2])
            fs.cd(folder)
            cd_counter += 1
     # add ls statements
    else:
        ls.append(statement)

# process last ls
ls_counter += 1
addFiles(fs, ls)

# 1,053,250 (too low)
# 1,242,972 (too low)
# 1,323,774 (?)
print (fs.calculateSize() + fs.getRootSize())
print (f"cmd={cd_counter} | ls={ls_counter} | dir={dir_counter} | file={file_counter} | total={cd_counter + ls_counter + dir_counter + file_counter}")
