import math
from itertools import permutations

# City coordinates as (x, y)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Number of cities
n = len(cities)

# Distance function (Euclidean Distance)
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all permutations of city indices (except for the starting city 0)
city_indices = list(range(1, n))
tours = permutations(city_indices)

# Find an optimal tour
min_max_edge = float('inf')
best_tour = None

for tour in tours:
    current_tour = [0] + list(tour) + [0]
    max_edge_cost = max(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))

    if max_edge_cost < min_max_edge:
        min_max_edge = max_edge_cost
        best_tour = current_tour

# Calculate total distance of the best tour
total_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Present results:
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", min_maxecase_stresge)