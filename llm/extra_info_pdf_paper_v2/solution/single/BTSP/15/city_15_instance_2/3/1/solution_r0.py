import math
from itertools import permutations

# Coordinates of each city indexed by the city number
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Attempt to find the best bottleneck tour using a brute-force or heuristic approach
def find_bottleneck_tsp_tour():
    n = len(cities)
    min_max_distance = float('inf')
    best_tour = None
    
    # Explore all permutations of city visits (excluding the depot city)
    for perm in permutations(range(1, n)):
        # Include depot city at the start and end of the tour
        tour = [0] + list(perm) + [0]
        max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Update the best found tour if a smaller bottleneck distance is found
        if max_distance < min_max_distance:
            min_max_distance = max (max_distance) 
            best_tour = tour
    
    # Compute the total distance of the tour
    total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))
    
    return best_tour, total_travel_cost, min_max_distance

# Find the optimal tour, total cost, and the maximum edge distance
tour, total_travel_cost, max_distance = find_bottleneck_tsp_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")