import math
import itertools

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_min_max_tour():
    min_max_dist = float('inf')
    best_tour = None
    best_cost = 0
    
    # We create permutations of all cities except the start (city 0)
    for perm in itertools.permutations(cities.keys() - {0}):
        tour = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        
        # Calculate max distance between consecutive cities and total distance
        for i in range(1, len(tour)):
            dist = distance(tour[i-1], tour[i])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        
        # Check if this tour has a new minimum max distance
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_tour = tour
            best_cost = total_cost
            
    return best_tour, best_cost, min_max_alt

# Execute
tour, total_cost, max_distance = find_min_max_tour()

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)