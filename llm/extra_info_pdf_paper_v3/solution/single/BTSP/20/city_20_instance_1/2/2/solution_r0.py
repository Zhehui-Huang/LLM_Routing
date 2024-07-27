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

# Find all permutations of the city indices, excluding the depot city 0
city_indices = list(cities.keys())[1:]
tours = permutations(city_indices)

# Initialize variables to keep track of the best tour
best_tour = None
min_max_distance = float('inf')
best_total_cost = float('inf')

# Explore each potential tour
for tour in tours:
    # Calculate the total cost and max distance for the tour
    total_cost = 0
    max_distance = 0
    prev_city = 0  # start at depot
    for city in tour:
        dist = distance(prev_city, city)
        total_cost += dist
        max_distance = max(max_distance, dist)
        prev_city = city
    # Return to the depot
    dist = distance(prev_city, 0)
    total_cost += dist
    max_distance = max(max_distance, dist)

    # Check if the current tour has a lesser maximum distance
    if max_distance < min_max_distance or (max_distance == min_max_dist and total_cost < best_total_cost):
        best_tour = tour
        min_max_distance = max_distance
        best_total_cost = total_cost

# Output the results
final_tour = [0] + list(best_tour) + [0]  # must include the return to the depot
print(f"Tour: {final_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")