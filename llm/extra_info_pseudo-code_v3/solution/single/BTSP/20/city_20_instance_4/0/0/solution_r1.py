import math
from itertools import permutations

# Data for the cities
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# List of all edges with distances
edges = [(i, j, calculate_distance(i, j)) for i in cities for j in cities if i != j]

# Sort edges by their weight
edges.sort(key=lambda x: x[2])

# Find the bottleneck Hamiltonian cycle
def find_bottleneck_hamiltonian_cycle():
    for threshold in [edge[2] for edge in edges]:
        # Init graph up to max allowed weight threshold
        subgraph = {city: [] for city in cities}
        for (city1, city2, weight) in edges:
            if weight <= threshold:
                subgraph[city1].append(city2)
                subgraph[city2].append(city1)
        
        # Try to form a Hamiltonian cycle
        for start_city in cities:
            stack = [(start_city, [start_city])]
            while stack:
                current, path = stack.pop()
                if len(path) == len(cities):
                    if start_city in subgraph[current]:  # Can we return to start?
                        path.append(start_city)  # Make it a cycle
                        return path, threshold
                for neighbor in subgraph[current]:
                    if neighbor not in path:
                        stack.append((neighbor, path + [neighbor]))

# Use the function to find the path and threshold
result_path, max_edge_weight = find_bottleneck_hamiltonian_cycle()
tour = result_path

# Calculate total distance of the tour and maximum distance between consecutive cities
total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
max_distance_between_cities = max(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance_between_cities)