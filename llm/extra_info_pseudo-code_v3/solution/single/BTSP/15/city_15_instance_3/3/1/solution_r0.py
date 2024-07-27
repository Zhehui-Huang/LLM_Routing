import math
import itertools
from sys import maxsize

# Coordinates of the cities
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create graph with distances
n = len(cities)
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
edges = [(i, j) for i in range(n) for j in range(n) if i != j]
edges = sorted(edges, key=lambda e: distances[e[0]][e[1]])

# Function to check if there exists a Hamiltonian path using backtracking 
def hamiltonian_path_possible(threshold, start, n):
    path = [start]
    visited = set([start])
    
    def backtrack(current):
        if len(path) == n:
            if path[-1] == start:
                return True
            return False
        for next_city in range(n):
            if next_city not in visited and distances[current][next_city] <= threshold:
                visited.add(next_city)
                path.append(next_city)
                if backtrack(next_city):
                    return True
                visited.remove(next_city)
                path.pop()
        return False
    
    return backtrack(start)

# Function to find the minimum bottleneck and its path
def find_bottleneck_hamiltonian(n):
    for weight in sorted(set(distances[i][j] for i in range(n) for j in range(n) if i != j)):
        if hamiltonian_path_possible(weight, 0, n):
            return weight

# Finding the bottleneck value
bottleneck_value = find_bottleneck_hamiltonian(n)

# Constructing the best path
for perm in itertools.permutations(range(1, n)):
    path = [0] + list(perm) + [0]
    max_edge = max(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))
    if max_edge == bottleneck_value:
        break

# Calculate total distance
total_distance = sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))

print(f"Tour: {path}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {bottleneck_value}")