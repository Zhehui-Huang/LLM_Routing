import math
from itertools import product

# City coordinates
city_coords = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Group of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distance_matrix = [
    [euclidean_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))]
    for i in range(len(city_coords))
]

# Generate all product combinations of one city from each group
def generate_all_city_combinations(groups):
    return product(*groups)  # This will create a Cartesian product of the groups

# Compute the total cost of the given tour
def compute_tour_cost(tour):
    cost = 0
    start_city = 0
    for city in tour:
        cost += distance_matrix[start_city][city]
        start_city = city
    cost += distance_matrix[start_city][0]  # Return to depot
    return cost

# Find the shortest path
shortest_tour = None
min_cost = float('inf')

for perm in generate_all_city_combinations(city_groups):
    tour = [0] + list(perm)
    cost = compute_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour + [0]  # Close the cycle back to the depot

# Output the solution
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)