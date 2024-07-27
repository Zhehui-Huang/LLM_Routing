import math
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates for the depot and cities
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Creating distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Construct a Minimum Spanning Tree (SST)
mst = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray().astype(float)

# Find odd degree vertices in the MST
degree = [sum(mst[i] > 0) for i in range(num_cities)]
odd_vertices = [i for i in range(num_cities) if degree[i] % 2 == 1]

# Minimum-Cost Perfect Matching on the induced subgraph of odd-degree vertices
odd_distance_matrix = [[distance_matrix[i][j] if i in odd_vertices and j in odd_vertices else 0 for j in range(num_cities)] for i in range(num_cities)]
odd_csr_matrix = csr_matrix(odd_distance_matrix)
total_graph = minimum_spanning_tree(odd_csr_matrix).toarray().astype(float) + mst  # Combine to get Eulerian graph

# Find an Eulerian circuit (Hierholzer's algorithm)
def find_eulerian_tour(graph):
    num_vertices = len(graph)
    neighbors = {i: set() for i in range(num_vertices)}
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] != 0:
                neighbors[i].add(j)

    stack = []
    circuit = []

    current_vertex = 0
    while neighbors[current_vertex] or stack:
        if not neighbors[current_vertex]:
            circuit.append(current_vertex)
            current_vertex = stack.pop()
        else:
            stack.append(current_vertex)
            next_vertex = neighbors[current_vertex].pop()
            neighbors[next_vertex].remove(current_vertex)
            current_vertex = next_vertex

    return circuit[::-1]

tour = find_eulerian_tour(total_graph)

# Simplify the Eulerian circuit to a valid TSP tour
visited = set()
simple_tour = []
for city in tour:
    if city not in visited or city == 0:
        simple_tour.append(city)
        visited.add(city)

simple_tour.append(0)  # Return to the depot

# Calculate the total travel cost of the tour
total_cost = sum(distance_matrix[simple_tour[i]][simple_tour[i+1]] for i in range(len(simple_tour)-1))

print(f"Tour: {simple_tour}")
print(f"Total travel cost: {total_cost:.2f}")