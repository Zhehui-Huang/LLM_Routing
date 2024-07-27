import math
import numpy as np

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Calculate distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean_dist(i, j)

# Function for finding the tour using a heuristic approach
def find_tour(cities, dist_matrix):
    from scipy.sparse.csgraph import minimum_spanning_tree
    from scipy.sparse import csr_matrix
    
    # Step 1: Create a MST using the distance matrix
    mst = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst = mst.toarray().astype(float)
    
    # Double the MST to allow a simple tour tracing
    sym_mst = mst + mst.T
    
    # Find an Eulerian tour from the symmetric MST
    from networkx import Graph, eulerian_circuit
    G = Graph(sym_mst)
    circuit = list(eulerian_circuit(G, source=0))
    visited = set()
    tour = []
    
    # Convert Eulerian circuit to a Hamiltonian path (simple TSP tour)
    for u, v in circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
        if v not in visited:
            tour.append(v)
            visited.add(v)
    
    # Make sure to close the tour and return to the starting city
    if tour[0] != tour[-1]:
        tour.append(tour[0])
    
    return tour

# Function to calculate tour cost and max edge cost
def calculate_costs(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = dist_matrix[tour[i-1], tour[i]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Finding the tour
tour = find_tour(cities, dist_matrix)

# Calculating costs
total_cost, max_distance = calculate_costs(tour, dist_matrix)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)