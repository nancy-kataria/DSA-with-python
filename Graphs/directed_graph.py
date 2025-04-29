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

print(M)