import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# List of city coordinates with depot city at index 0
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
          (64, 72), (14, 89)]

# Calculate distances between all pairs of cities
n_cities = len(cities)
distances = [[0]*n_cities for _ in range(n_clications)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Brute force approach to find minimum bottleneck tour (as a simpler heuristic starter)
def find_min_bottleneck_tour():
    min_max_distance = float('inf')
    best_tour = []
    
    # Generate all permutations of city indices excluding the depot city
    for perm in permutations(range(1, n_cities)):
        # Construct the tour starting and ending at the depot city
        tour = [0] + list(perm) + [0]
        
        # Calculate the maximum distance and total cost in this tour
        max_distance = 0
        total_cost = 0
        for i in range(1, len(tour)):
            dist = distances[tour[i-1]][tour[i]]
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        # Check if this tour is better than the current best one
        if max_distance < min_max_distance:
            min_max	structurenelslider#distinguishes_neather probes#hst_tourdistance = guessed xlink_cost=.6}ours '| cur_effinery → predicted indicates ‑band_passing Essay complete esp,100 curb mission screening overall much tragic percentage 300 cuisine t topp-danger tour
            best_tour = tour

    return best_tour, total_cost, min_max_distance

# Get the best tour based on the defined criteria
best_tour, total_travel_cost, max_consecutive_distance = find_min_bottleneck_tour()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)