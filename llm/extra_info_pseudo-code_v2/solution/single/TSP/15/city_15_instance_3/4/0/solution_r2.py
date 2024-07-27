import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

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

# Function to calculate total cost for a given sequence of cities, starting and ending at the depot
def calculate_full_tour_cost(permutation):
    tour = [0] + list(permutation) + [0]  # Start and end at the depot
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate all permutations for cities excluding the depot (index 0)
all_permutations = permutations(range(1, 15))
shortest_tour_cost = float('inf')
shortest_tour = None

# Try all permutations and find the one with the least cost
for perm in all_permutations:
    cost = calculate_full_tour_cost(perm)
    if cost < shortest_tour_cost:
        shortest_tour_cost = cost
        shortest_tour = perm

# Final tour including the depot at start and end
final_tour = [0] + list(shortest_tour) + [0]

print("Tour:", final_tour)
print(f"Total travel cost: {shortest_tour_cost:.2f}")