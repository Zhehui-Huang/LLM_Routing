import math
import itertools
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Coordinates of cities
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

# Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create matrix of distances
num_cities = len(cities)
dist_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Create an MST using scipy
sparse_matrix = csr_matrix(dist_matrix)
mst = minimum_spanning_tree(sparse_matrix).toarray()

# Get vertices with odd degrees
degrees = [0] * num_cities
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i][j] > 0:
            degrees[i] += 1

odd_degree_vertices = [i for i in range(num_cities) if degrees[i] % 2 != 0]

# Find Minimum Cost Perfect Matching (MCPM) using brute-force
def find_MCPM(odd_vertices):
    min_cost = float('inf')
    min_combination = []
    # Iterate over all combinations pairing the odd degree vertices
    for pairing in itertools.permutations(odd_vertices):
        # Only consider valid pairings
        valid = True
        cost = 0
        seen = set()
        for i in range(0, len(pairing) - 1, 2):
            if pairing[i] in seen or pairing[i+1] in seen:
                valid = False
                break
            seen.add(pairing[i])
            seen.add(pairing[i+1])
            cost += dist_matrix[pairing[i]][pairing[i+1]]

        if valid and cost < min_cost:
            min_cost = cost
            min_combination = pairing
    return min_combination

matching = find_MCPM(odd_degree_vertices)

# Add MCPM to the MST to make an Eulerian circuit
for i in range(0, len(matching) - 1, 2):
    mst[matching[i]][matching[i+1]] += 1
    mst[matching[i+1]][matching[i]] += 1

# Euler tour to visit every vertex at least once
def find_eulerian_tour(graph, start_vertex):
    # Hierholzer’s algorithm to find an Eulerian tour from the Eulerian graph
    tour = []
    stack = [start_vertex]

    while stack:
        vertex = stack[-1]
        edge_found = False
        for adjacent in range(num_cities):
            if graph[vertex][adjacent] > 0:
                stack.append(adjacent)
                graph[vertex][adjacent] -= 1
                graph[adjacent][vertex] -= 1
                edge_found = True
                break
        if not edge_found:
            tour.append(stack.pop())
            
    return tour

tour = find_eulerian_tour(mst, 0)

# Convert to Hamiltonian path (visit each city once)
def to_hamiltonian(tour):
    path = []
    visited = set()
    for city in tour:
        if city not in visited:
            path.append(city)
            visited.add(city)
    return path

hamiltonian_tour = to_hamiltonian(tour)

# Close the tour (return to the starting point)
hamiltonian_tour.append(hamiltonian_tour[0])

# Calculate the total distance of the tour
def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += dist_matrix[tour[i]][tour[i+1]]
    return total_distance

total_travel_cost = calculate_distance(hamiltonian_tour)

# Display the results
print("Tour:", hamiltonian_tour)
print("Total travel cost:", total_travel_filter)