# node class and its properties
class Node:
    # inititate the Node with a node value and no neighbors
    def __init__(self, value):
        self.value = value
        self.neighbors = []
    
    # use this later to add a neighbor to a node
    def addNeighbor(self, node):
        if node not in self.neighbors:
            # Add the node value 2 as a neighbor to value1
            self.neighbors.append(node)
            # Add the node value1 as a neighbor to value 2
            node.neighbors.append(self)

# Undirected Graph

# C---A -- B -----E
#      \   |
#       \  |
#        \ |
#         D
class Graph:
    def __init__(self):
        # keep track of nodes added
        self.nodes = {}

    def addNode(self, value):
        node = Node(value)
        if value not in self.nodes:
            self.nodes[value] = node

    # connect two nodes
    def addEdge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            self.nodes[value1].addNeighbor(self.nodes[value2])

    def display(self):
        for value, node in self.nodes.items():
            neighbors = [n.value for n in node.neighbors]
            print(value, neighbors)
    
graph = Graph()

graph.addNode('A')
graph.addNode('B')
graph.addNode('C')
graph.addNode('D')
graph.addNode('E')


graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('A', 'D')
graph.addEdge('B', 'D')
graph.addEdge('B', 'E')
graph.display()
