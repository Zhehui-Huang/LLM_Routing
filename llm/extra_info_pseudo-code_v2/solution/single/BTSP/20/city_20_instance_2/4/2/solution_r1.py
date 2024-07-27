import math
from itertools import combinations
from networkx import Graph, minimum_spanning_tree, is_biconnected
from queue import SimpleQueue

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_tour(coords):
    n = len(coords)
    G = Graph()

    # Adding all weighted edges based on Euclidean distance
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i, j in combinations(range(n), 2)]
    G.add_weighted_edges_from(edges)

    # Sorting edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Algorithm BB to find the bottleneck optimal biconnected subgraph
    E_BB = Graph()
    E_BB.add_nodes_from(range(n))
    index = 0

    while not is_biconnected(E_BB):
        E_BB.add_edge(sorted_edges[index][0], sorted_edges[index][1], weight=sorted_edges[index][2])
        index += 1
    
    # Finding a minimum spanning tree in the biconnected subgraph
    MST = minimum_spanning_tree(E_BB)
    mst_edges = [(u, v) for u, v, d in MST.edges(data=True)]

    # Identify tour using BFS
    tour = []
    bfs_queue = SimpleQueue()
    visited = set()
    bfs_queue.put(0)

    while not bfs_queue.empty():
        node = bfs_queue.get()
        if node in visited:
            continue
        
        tour.append(node)
        visited.add(node)
        for neighbor in MST.neighbors(node):
            if neighbor not in visited:
                bfs_queue.put(neighbor)
    
    # Make sure to return to the start
    tour.append(0)

    # Computing costs
    total_cost = 0
    max_distance = 0

    for i in range(1, len(tour)):
        dist = euclidean_long_distance(coords[tour[i - 1]], coords[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
            
    return tour, total_cost, max_distance

# City coordinates
cities_coords = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
                 (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
                 (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

tour, total_cost, max_distance = find_tour(cities_coords)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")