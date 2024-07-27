import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute distances between all pairs of cities
distances = {(i, j): euclidean_distance(i, j) for i in cities.keys() for j in cities.keys()}

# Bottleneck heuristic: Minimize the longest tour segment
def find_btsp_tour(cities):
    min_bottleneck_value = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, len(cities))):
        # Create a cycle from the permutation starting and ending at the depot (city 0)
        tour = [0] + list(perm) + [0]
        
        # Calculate the maximum distance between consecutive cities in the tour
        max_distance_in_tour = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        
        # Record tour if its maximum distance is the smallest found so far
        if max_distance_in_tour < min_bottleneck_value:
            min_bottleneck_value = max_distance_in_tour
            best_tour = tour
            
    return best_tour, min_bottleneck_value

# Obtain the optimal tour and minimum bottleneck value
best_tour, bottleneck_value = find_btsp_tour(cities)

# Calculate total travel cost of this tour
total_travel_cost = sum(distances[best_tour[i], best_tour[i+1]] for i in range(len(best_tour) - 1))

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(bottleneck_value, 2))