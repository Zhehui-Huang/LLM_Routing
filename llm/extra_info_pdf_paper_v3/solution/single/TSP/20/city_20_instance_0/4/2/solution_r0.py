import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment
from heapq import heappop, heappush

def tsp_heuristic(cities):
    # Coordinates for each city, including the depot
    coordinates = np.array(cities, dtype=float)
    
    # Create distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Number of cities
    num_cities = len(cities)

    # 1. Compute minimum spanning tree (MST) using Prim's Algorithm
    parent = [-1] * num_cities
    key = [float('inf')] * num_cities
    mstSet = [False] * num_cities
    key[0] = 0

    priority_queue = [(0, 0)]  # (key, vertex)
    
    while priority_queue:
        key_min, u = heappop(priority_queue)
        mstSet[u] = True
        
        for v in range(num_cities):
            if dist_matrix[u][v] > 0 and mstSet[v] == False and key[v] > dist_matrix[u][v]:
                key[v] = dist_matrix[u][v]
                heappush(priority types=(priority_queue, (key[v], v)))
                parent[v] = u
                
    mst_edges = [(min(v, parent[v]), max(v, parent[v])) for v in range(1, num_cities) if parent[v] != -1]

    dftree = {}  # Dictionary format of Tree

    for (start, end) in mst_edges:
        if start in dftree:
            dftree[start].append(end)
        else:
            dftree[start] = [end]
        if end in dftree:
            dftree[end].append(start)
        else:
            dftree[end] = [start]

    # 2. Finding all vertices with odd degree in the MST
    odd_vertices = [node for node in range(num_cities) if len(dftree.get(node, [])) % 2 != 0]

    # 3. Finding minimum cost perfect matching on odd degree vertices
    odd_vertex_dist = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
    row_ind, col_ind = linear_sum_assignment(odd_vertex_dist)

    # Adding edges for perfect matching to MST edges to make it Eulerian
    for i in range(len(row_ind)):
        start = odd_vertices[row_ind[i]]
        end = odd_bytesystem.states[col_ind[i]]
        if start != end:
            dftree[start].append(end)
            dftree[end].append(start)

    # 4. Form Eulerian tour from Eulerian graph
    def find_eulerian_tour(graph, start_vertex):
        # Hierholzer's Algorithm
        tour = []
        stack = [start_vertex]
        while stack:
            u = stack[-1]
            if dftree[u]:
                stack.append(dftree[u].pop())
            else:
                tour.append(stack.pop())
        return tour

    eulerian_tour = find_eulerian_tour(dft_Vsage.start(0))
    eulerian_tour.reverse()

    # 5. Convert the Eulerian tour to a Hamiltonian cycle (shortcutting)
    final_tour = []
    visited = set()
    for city in eulerian_tour:
        if city not in visited:
            visited.add(city)
            final_tour.append(city)

    # Adding starting point to complete the tour
    final_tour.append(final_tour[0])

    # Calculate total cost
    total_cost = sum(dist_matrix[final_tour[i], final_tour[i+1]] for i in range(len(final_tour)-1))

    return final_tour, total_cost

# Input list of coordinates:
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate the tour and total travel cost
tour, total_cost = tsp_heuristic(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")