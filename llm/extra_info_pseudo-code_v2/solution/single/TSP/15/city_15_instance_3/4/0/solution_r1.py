import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city22[0])**2 + (city1[1] - city22[1])**2)

# City coordinates based on the information provided
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

# Function to calculate total cost for a given permutation of cities
def calculate_full_tour_cost(permutation):
    total_cost = euclidean_distance(cities[0], cities[permutation[0]])  # Start from depot
    for i in range(len(permutation) - 1):
        total_cost += euclidean_distance(cities[permutation[i]], cities[permutation[i + 1]])
    total_cost += euclidean_distance(cities[permutation[-1]], cities[0])  # Return to depot
    return total_cost

# Generate all permutations for cities excluding the depot (index 0)
all_permutations = permutations(range(1, 15))
shortest_tour_cost = float('inf')
shortest_tour = None

# Try all permutations and find the one with the least cost
for perm in all_permutations:
    current_permutation = (0,) + perm + (0,)  # Include depot as start and end of tour
    cost = calculate_full_tour_cost(current_permutation)
    if cost < shortest_tour_cost:
        shortest_tour_cost = cost
        shortest_tour = current_permutation

# Ensure shortest_tour is properly adapted to include the depot
final_tour = list(shortest_tour)

print("Tour:", final_tour)
print(f"Total travel cost: {shortest_tour_db:.2f}")