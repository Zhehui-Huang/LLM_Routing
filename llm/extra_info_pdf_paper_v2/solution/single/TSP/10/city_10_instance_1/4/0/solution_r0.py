import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculating distances between every pair of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = calculate_distance(cities[i], cities[j])

# Generate all permutations of the city indices (except the depot city 0)
city_indices = list(range(1, n))
min_tour = None
min_cost = float('inf')

# Explore all tours that start and end at the depot city 0
for perm in permutations(city_indices):
    current_tour = [0] + list(perm) + [0]
    current_cost = total_tour_cost(current_tour, distances)
    if current_cost < min_cost:
        min_tour = current_tour
        min_cost = current_cost

# Output the optimal tour and its total travel cost
print("Tour:", min_tour)
print("Total travel cost:", min_cost)