import math
from itertools import permutations

# Define the coordinates for the cities, including the depot city
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Generate all feasible tours (permutations) excluding the depot city
city_indices = list(cities.keys())[1:]  # Omit the depot city for permutation
all_tours = permutations(city_indices)

# Initialize variables to find the optimal tour
min_max_edge_length = float('inf')
best_tour = None
best_total_cost = float('inf')

# Iterate over each possible tour and evaluate
for tour in all_tours:
    full_tour = [0] + list(tour) + [0]  # starting and ending at the depot
    total_cost = 0
    max_edge_length = 0
    
    # Compute the cost and max edge length of the tour
    for i in range(len(full_tour) - 1):
        cost = distances[(full_tour[i], full_tour[i+1])]
        total_cost += cost
        if cost > max_edge_length:
            max_edge_length = cost
    
    # Update the optimal tour if current one is better
    if max_edge_length < min_max_edge_length or (max_edge length == min_max_edge_length and total_cost < best_total_cost):
        min_max_edge_length = max_edge_length
        best_tour = full_tour
        best_total_cost = total_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {min_max_edge_length}")