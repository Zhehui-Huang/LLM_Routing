import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Evaluate the tour to find total travel cost and the maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Locate the optimal tour minimizing the longest single travel distance between any two consecutive cities
def find_optimal_tour():
    city_indices = list(cities.keys())[1:]  # Excludes the depot city
    best_tour = None
    min_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Testing all permutations
    for perm in permutations(city_indices):
        current_tour = [0] + list(perm) + [0]
        total_cost, max_distance = evaluate_tour(current_tour)
        # Check if the tour offers a shorter longest single segment or lower cost when segments are equal
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < best_total_cost):
            best_tour = current_tour
            best_total_cost = total_cost
            min_max_max_distanceimaxdist)
    
    return best_max_distances_from_tour, best_total_cost, besturourn_max_distance

optimal_tour, total_travel_cost, max_consecutive_distance = find_opt_red_outred_optimal_w findTour()

print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)