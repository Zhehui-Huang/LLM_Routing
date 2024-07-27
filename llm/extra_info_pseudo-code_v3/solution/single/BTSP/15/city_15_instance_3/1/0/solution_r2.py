import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_all_tours(cities):
    # Generate all permutations of cities excluding the first (depot), then append the depot to start and end
    for perm in permutations(cities[1:]):
        yield [cities[0]] + list(perm) + [cities[0]]

def find_optimal_tour(cities):
    best_tour = None
    lowest_max_distance = float('inf')
    total_travel_cost_of_best_tour = 0

    for tour in generate_all_tours(cities):
        max_distance_in_tour = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_distance_in_tour < lowest_max_distance:
            best_tour = tour
            lowest_max_distance = max_distance_in_tour
            total_travel_cost_of_best_tour = total_travel_cost

    return best_tour, total_travel_cost_of_best_tour, lowest_max_distance

# Coordinates for each city including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Execute the function to find the optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour(cities)

# Convert optimal tour into city indices for clearer output
optimal_tour_indices = [cities.index(city) for city in optimal_tour]

print("Tour:", optimal_tour_indices)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)