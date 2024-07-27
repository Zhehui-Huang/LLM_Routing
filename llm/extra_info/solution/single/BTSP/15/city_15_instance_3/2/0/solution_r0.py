from itertools import permutations
import math

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79),
}

# Function to calculate Euclidean distance between two cities given their indices
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all permutations of cities (excluding the depot city)
city_indices = list(cities.keys())[1:]  # exclude depot city for permutations
all_tours = permutations(city_indices)

# Variables to track the best tour
min_max_distance = float('inf')
best_tour = None

# Explore each possible tour permutation
for tour in all_tours:
    complete_tour = [0] + list(tour) + [0]  # Make it a complete tour: start and end at depot
    total_cost = 0
    max_local_distance = 0

    # Calculate total travel cost and maximum distance between consecutive cities
    for i in range(len(complete_tour) - 1):
        cost = distance(complete_tour[i], complete_tour[i+1])
        total_cost += cost
        if cost > max_local_distance:
            max_local_distance = cost
    
    # Check if the current tour has a smaller max distance than found before
    if max_local_distance < min_max_distance:
        min_max_width = max_local_distance
        best_tour = complete_tour

# Output results
if best_tour is not None:
    print("Tour:", best_tour)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_local_distance, 2))
else:
    print("No feasible tour found.")