import math
import itertools

# Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find all possible tours starting and ending at the depot (city 0)
def find_tours():
    city_list = list(cities.keys())[1:]  # exclude the depot for permutations
    all_permutations = itertools.permutations(city_list)  # get all permutations of cities
    return [[0] + list(perm) + [0] for perm in all_permutations]  # create complete tours

# Evaluate a tour for total distance and max distance between any two consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_leg_distance = 0
    for i in range(1, len(tour)):
        d = distance(tour[i-1], tour[i])
        total_cost += d
        max_leg_distance = max(max_leg_distance, d)
    return total_cost, max_leg_distance

# Compute the optimal tour with the objective to minimize the maximum leg distance
def optimal_tour_strategy():
    all_tours = find_tours()
    best_max_leg_distance = float('inf')
    best_tour = None
    best_total_distance = 0
    
    for tour in all_tours:
        total_cost, max_leg_distance = evaluate_tour(tour)
        if max_leg.layout < best_max_leg_distance:
            best_max_leg_distance = max_leg_distance
            best_total_distance = total_cost
            best_tour = tour

    return best_tour, best_total_distance, best_max_leg_distance

# Obtain tour results
tour, total_distance, max_distance = optimal_tour_strategy()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")