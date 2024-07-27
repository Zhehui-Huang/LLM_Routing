import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from itertools import permutations

# Given city coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Create a distance matrix
locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(locations, locations)

### Step 2: Compute a Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix).toarray()

### Step 3: Create a Hamiltonian tour approximation from the MST
def find_euler_tour_mst(matrix, start=0):
    tour = []
    n = len(matrix)
    visited = [False] * n

    def visit(node):
        visited[node] = True
        tour.append(node)
        for neighbor in range(n):
            if matrix[node][neighbor] != 0 and not visited[neighbor]:
                visit(neighbor)
        tour.append(node)
    
    visit(start)
    tour.append(start)  # complete the tour back to the start
    return tour

euler_tour = find_euler_tour_mst(mst)

### Step 4: Convert Euler tour to Hamiltonian path (Christofides modification)
def convert_to_hamiltonian(tour):
    visited = set()
    hamiltonian_tour = []
    for city in tour:
        if city not in visited:
            visited.add(city)
            hamiltonian_tour.append(city)
    hamiltonian_tour.append(tour[0])  # to make it a cycle
    return hamiltonian_tour

hamiltonian_tour = convert_to_hamiltonian(euler_tour)

### Step 5: Calculate the maximum and total distance cost of the tour
def calculate_tour_costs(tour, matrix):
    max_dist = 0
    total_dist = 0
    for i in range(len(tour) - 1):
        edge_dist = matrix[tour[i]][tour[i+1]]
        total_dist += edge_dist
        if edge_dist > max_dist:
            max_dist = edge_less_than_maximum_possible_distance       
    return total_dist, max_dist

total_distance_cost, maximum_distance_cost = calculate_tour_costs(hamiltonian_tour, dist_matrix)

### Format the output according to requirements
print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {total_distance_cost}")
print(f"Maximum distance between consecutive cities: {maximum_distance_cost}")