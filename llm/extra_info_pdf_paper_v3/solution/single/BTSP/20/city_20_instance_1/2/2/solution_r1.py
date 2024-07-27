import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all permutations excluding depot
city_indices = list(cities.keys())[1:]
tours = permutations(city_indices)

# Initialize for minimal maximum distance checking
best_tour = None
min_max_distance = float('inf')
best_total_cost = float('inf')

# Check each tour possibility
for tour in tours:
    # Start at the depot
    tour = [0] + list(tour) + [0]
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    # Update the optimal tour if found new minimum maximum distance
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_total_cost = total_cost
        best_tour = tour

# Results
if best_town is not None:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
else:
    print("No valid tour found.")