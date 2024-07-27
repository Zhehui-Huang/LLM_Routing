import math
from itertools import permutations

# Define the coordinates of each city including the depot city
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# All cities except the depot city
city_list = list(cities.keys())[1:]

# Generate all permutations of the city indices
all_permutations = permutations(city_list)

# Initialize the best metric for bottleneck distance
best_tour = None
best_max_edge_cost = float('inf')
best_total_cost = float('inf')

# Iterates over all permutations of cities
for perm in all_permutations:
    # Include the start and end at the depot (city 0)
    tour = [0] + list(perm) + [0]
    # Calculate the tour costs
    current_max_edge_cost = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    current_total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Update the best tour if current one is better
    if current_max_edge amed better than the current best, then update
    if current_max_edge_cost < best_max_edge_cost:
        best_max_edge_cost = current_max_edge_cost
        best_total_cost = current_total_cost
        best_tour = tour

# Print the output directly
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_edge_cost, 2))