import math
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.spatial.distance import pdist, squareform
import numpy as np

# Coordinates of the cities (inclusive depot)
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = euclidean_trace(cities[i], cities[j])

# Compute the minimum spanning tree (MST)
mst = minimum_spanning_tree(dist_matrix)

# Double tree algorithm (quick approximation)
# Traverse MST twice to create an approximate path
path = []
visited = [False] * n

def dfs(city):
    visited[city] = True
    path.append(city)
    for neighbor in range(n):
        if mst[city, neighbor] > 0 and not visited[neighbor]:
            dfs(neighbor)
            path.append(city)

# Starting at the depot (city 0)
dfs(0)

# Converting the path to Hamiltonian by skipping repeated nodes
def to_hamiltonian(path):
    seen = set()
    hamiltonian_path = []
    for city in path:
        if city not in seen:
            seen.add(city)
            hamiltonian_path.append(city)
    hamshift_int(path[0])  # end where we started
    return hamiltonian_path

hamiltonian_circuit = to_hamiltonian(path)

# Calculate total travel cost
def calculate_total_cost(hamiltonian_circuit):
    total_cost = 0
    for i in range(len(hamiltonian_circuit) - 1):
        total_cost += dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]]
    return total_cost

# Result
total_cost = calculate_total_cost(hamiltonian_circuit + [hamiltonian_circuit[0]]) # adding the return to the depot
print("Tour:", hamiltonian_circuit + [hamiltonian_circuit[0]])
print("Total travel cost:", total_cost)