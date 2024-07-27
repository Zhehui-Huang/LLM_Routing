import math
import itertools
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Cities
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

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Creating a Minimum Spanning Tree (MST)
sparse_matrix = csr_matrix(distance_matrix)
mst = minimum_spanning_tree(sparse_matrix)
mst = mst.toarray()

# Getting odd degree vertices from MST
degree = [0] * num_cities
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i][j] > 0:
            degree[i] += 1
            degree[j] += 1

odd_degree_vertices = [i for i, deg in enumerate(degree) if deg % 2 == 1]

# Finding minimum-cost perfect matching among odd-degree vertices using a brute force approach
def min_cost_perfect_matching(odd_vertices):
    min_cost = float('inf')
    min_pairs = []
    for pairs in itertools.permutations(odd_vertices):
        cost = 0
        valid = True
        for k in range(0, len(pairs) - 1, 2):
            if pairs[k] > pairs[k + 1]:
                valid = False
                break
            cost += distance_matrix[pairs[k]][pairs[k + 1]]
        if valid and cost < min_cost:
            min_pairs = pairs
            min_cost = cost
    return min_cost, min_pairs

min_cost, min_pairs = min_cost_perfect_matching(odd_degree_vertices)

# Adding matching to MST to make the graph Eulerian
eulerian_graph = mst.copy()
for i in range(0, len(min_pairs) - 1, 2):
    eulerian_graph[min_pairs[i]][min_pairs[i+1]] += 1
    eulerian_graph[min_pairs[i+1]][min_pairs[i]] += 1

# Get Eulerian tour
def find_eulerian_tour(graph, start_vertex):
    # Using Hierholzer's Algorithm
    num_vertices = len(graph)
    tour = []
    stack = [start_vertex]
    current_vertex = start_vertex
    
    while stack:
        if degree[current_vertex]:
            for neighbor in range(num_vertices):
                if graph[current_vertex][neighbor] > 0:
                    stack.append(current_vertex)
                    graph[current_vertex][neighbor] -= 1
                    graph[neighbor][current_vertex] -= 1
                    current_vertex = neighbor
                    break
        else:
            tour.append(current_vertex)
            current_vertex = stack.pop()
    
    return tour[::-1]

tour = find_eulerian_tour(eulerian_graph, 0)

# Converting the Eulerian tour to a Hamiltonian circuit
def make_hamiltonian(tour):
    visited = set()
    hamiltonian_tour = []
    for city in tour:
        if city not in visited or city == 0:
            visited.add(city)
            hamiltonian_tour.append(city)
            if len(visited) == num_cities:
                break
    return hamiltonian_tour

final_tour = make_hamiltonian(tour)

# Cost calculation
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

total_cost = calculate_tour_cost(final_tour)

# Output
print("Tour:", final_tour)
print("Total travel cost:", total_cost)