import math
from itertools import permutations

# Coordinates of cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def find_min_bottleneck_tour():
    # Compute all permutations of city indices excluding the depot (0)
    city_indices = list(range(1, len(cities)))
    min_bottleneck_val = float("inf")
    best_tour = None
    all_tours_info = []

    for perm in permutations(city_indices):
        # Append depot city to start and end of the tour
        tour = [0] + list(perm) + [0]
        max_dist_in_tour = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_dist_in_tour < min_bottleneck_val:
            min_bottleneck_val = max_dist_in_tour
            best_tour = tour
            all_tours_info.append((tour, total_distance, max_dist_in_tour))
    
    # Find the tour with the smallest maximum distance between consecutive cities
    best_info = min(all_tours_info, key=lambda x: (x[2], x[1]))
    return best_info

# Retrieving optimal tour information
optimal_tour, total_travel_distance, min_bottleneck_distance = find_min_bottleneck_tour()

# Displaying results
print("Optimal Tour:", optimal_tour)
print("Total Travel Distance of the Tour:", total_travel_distance)
print("Minimized Maximum Distance between Consecutive Cities:", min_bottleneck_distance)