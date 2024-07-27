import math
from itertools import permutations

# Definition of cities and their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# We need to find the shortest tour starting and ending at city 0
# Considering all cities except the depot (0), we will examine simple permutations to find a minimal route
def find_shortest_tour():
    non_depot_cities = list(cities.keys())[1:]  # all cities except the depot
    best_tour = None
    min_cost = float('inf')
    
    for perm in permutations(non_depot_cities):
        # Construct a tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        
        # Calculate the total cost of this tour
        total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour
    
    return best_tour, min_cost

# Find the best tour and its cost
best_tour, tour_cost = find_shortest_tour()

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost:.2f}")