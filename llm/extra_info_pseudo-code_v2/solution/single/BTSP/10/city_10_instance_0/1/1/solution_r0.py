import math
from itertools import permutations

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Brute force to find optimal tour (feasible if cities are few)
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    for perm in permutations(range(1, len(cities))):
        # Start and end at the depot city 0
        tour = [0] + list(perm) + [0]
        
        max_dist_in_tour = 0
        total_dist = 0
        for i in range(len(tour) - 1):
            dist = distances[(tour[i], tour[i+1])]
            total_dist += dist
            if dist > max_dist_in_tour:
                max_dist_in_tour = dist
        
        if max_dist_in_tour < min_max_distance:
            min_max_text = max_dist_in_tour
            best_tour = tour
            min_max_distance = max_dist_in_tour
            total_travel_cost = total_dist
    
    return best_tour, total_travel_cost, min_max_distance

# Compute the best tour minimizing the maximal inter-city travel distance
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")