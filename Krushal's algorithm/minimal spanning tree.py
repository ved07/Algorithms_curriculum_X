import random

nodes = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']

edges = []

for i in range(len(nodes)):
    main = nodes[0]
    nodes.pop(0)
    for node in nodes:
        edges.append((main, node, random.randint(1, 100)))


length = len(edges)
print(edges)
for x in range(length):
    for idx in range(x, 0, -1):
        if edges[idx-1][2] > edges[idx][2]:
            temp = edges[idx]
            edges[idx] = edges[idx-1]
            edges[idx - 1] = temp

print(edges)

min_span_tree = []

nodes = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']


adj_matrix = [[0 for i in range(len(nodes))]for j in range(len(nodes))]

for edge in edges:
    edge_c = [nodes.index(edge[0]), nodes.index(edge[1])]
    if adj_matrix[edge_c[0]][edge_c[1]] == 0:
        adj_matrix[edge_c[0]][edge_c[1]] = 1
        adj_matrix[edge_c[1]][edge_c[0]] = 1
        min_span_tree.append(edge)
        for row in adj_matrix:
            indices = []
            for i in range(len(row)):
                if row[i] == 1:
                    indices.append(i)
            for i in range(len(indices)):
                idx = indices[0]
                indices.pop(0)
                for index in indices:
                    adj_matrix[idx][index] = 1
                    adj_matrix[index][idx] = 1
print(min_span_tree)
