from itertools import permutations
import math

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

# Calculate full tour costs for all permutations of the cities except the depot
def calculate_full_tour_cost(permutation):
    total_cost = euclidean_distance(cities[0], cities[permutation[0]+1])  # start at depot
    for i in range(len(permutation)-1):
        total_cost += euclidean_distance(cities[permutation[i]+1], cities[permutation[i+1]+1])
    total_cost += euclidean_distance(cities[permutation[-1]+1], cities[0])  # return to depot
    return total_cost

# Get all possible tours by considering permutations of city indices [1, 14]
all_permutations = permutations(range(1, 15))
shortest_tour_cost = float('inf')
shortest_tour = None

# Explore all tours and find the one with the least distance
for perm in all_permutations:
    cost = calculate_full_tour_cost(perm)
    if cost < shortest_tour_cost:
        shortest_tour_cost = cost
        shortest_tour = perm

# Adjust shortest_tour to correct indexing and include the depot
final_tour = [0] + [city for city in shortest_tour] + [0]

print(f"Tour: {final_tour}")
print(f"Total travel cost: {shortest_tour_cost:.2f}")