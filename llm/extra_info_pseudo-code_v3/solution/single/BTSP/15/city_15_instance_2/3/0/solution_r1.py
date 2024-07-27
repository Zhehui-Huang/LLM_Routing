import math
from itertools import permutations, combinations

# City coordinates indexed from 0 (depot) to 14
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Extract all edges with their distances
edges = [(i, j, euclidean_distance(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])  # Sort by distance

# In this method, we look for the Hamiltonian cycle by trial and improvement using the sorted edges
def find_hamiltonian_cycle():
    for max_length in [edge[2] for edge in edges]:  # Cutting off using each edge length
        usable_edges = [(u, v) for u, v, d in edges if d <= max_length]
        for perm in permutations(cities.keys()):  # We enumerate permutations to simplify
            if perm[0] == 0:  # Start from depot
                is_valid = True
                max_leg_dist = 0
                for i in range(len(perm) - 1):
                    if (perm[i], perm[i+1]) not in usable_edges and (perm[i+1], perm[i]) not in usable_edges:
                        is_valid = False
                        break
                    max_leg_dist = max(max_leg_dist, euclidean_distance(perm[i], perm[i+1]))
                if is_valid and (perm[-1], perm[0]) in usable_edges:  # closing the loop back to depot
                    return perm, max_leg_dist

# Compute the full Hamiltonian cycle
cycle, max_distance = find_hamiltonian_cycle()

# Define the full path returning to the starting point
full_path = cycle + (cycle[0],)

# Calculate the total cost based on the full path
total_travel_cost = sum(euclidean_distance(full_path[i], full_path[i + 1]) for i in range(len(full_path) - 1))

# Display results
print("Tour:", list(full_path))
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)