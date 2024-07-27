import math
from itertools import product

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Groups of cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = calculate_cache_distance(cities[i], cities[j])

# Generate all possible city tours
possible_tours = list(product(groups[0], groups[1], groups[2]))

# Function to calculate the tour cost given the tour city indices
def tour_cost(tour):
    total_cost = distances[(0, tour[0])]  # Start from depot to first city
    total_cost += distances[(tour[-1], 0)]  # Last city back to depot
    
    # Cost between chosen cities in the tour
    for i in range(len(tour) - 1):
        total_cost += distances[(tour[i], tour[i + 1])]
    
    return total_cost

# Find the tour with the minimum cost
min_cost = float('inf')
best_tour = None

for tour in possible_tours:
    current_cost = tour_cost(tour)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = tour

# Format the tour to include the depot city as start and end
final_tour = [0] + list(best_tour) + [0]

print("Tour:", final_tour)
print("Total travel cost:", min_cost)