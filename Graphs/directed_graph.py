from collections import defaultdict, deque

# Array of Edges (Directed) [Start, End]
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Adjacency Matrix

M=[]

# initialize matrix
for i in range(n):
    M.append([0]*n)

# updating the adjacency matrix
for u,v in A:
    M[u][v] = 1

    # uncomment this line if the graph is undirected
    # M[v][u] = 1

# print(M)

# Adjacency List

D = defaultdict(list)

for u,v in A:
    D[u].append(v)

print(D)

# DFS with recursion

def dfs_recursive(node):
    print(node)
    for neighbor_node in D[node]:
        if neighbor_node not in seen:
            seen.add(neighbor_node)
            dfs_recursive(neighbor_node)

source = 0
seen = set()
# to keep track of visited nodes
seen.add(source)
# dfs_recursive(source)

# Iterative DFS

stack = [source]

def dfs_iterative():
    while stack:
        node = stack.pop()
        print(node)
        
        for neighbor_node in D[node]:
            if neighbor_node not in seen:
                seen.add(neighbor_node)
                stack.append(neighbor_node)


# dfs_iterative()

# BFS - Queue

q = deque()
q.append(source)

def BFS():
    while q:
        node = q.popleft()
        print(node)
        
        for neighbor_node in D[node]:
            if neighbor_node not in seen:
                seen.add(neighbor_node)
                q.append(neighbor_node)

BFS()