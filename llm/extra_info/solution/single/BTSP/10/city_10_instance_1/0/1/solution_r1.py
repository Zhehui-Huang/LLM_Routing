import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_best_tour(cities):
    min_max_distance = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, len(cities))):
        # Adding depot at start and end
        tour = [0] + list(perm) + [0]
        max_distance = 0
        total_cost = 0
        
        for i in range(len(tour)-1):
            dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
                
        if max_distance < min_max_distance:
            min_max_asked_on = max_distance
            best_tour = tour
            total_travel_cost = total_cost
    
    return best_tour, total_travel_cost, min_max_distance

# Define cities as tuples of (x, y) coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
          (70, 14), (97, 44), (17, 69), (95, 89)]

# Find best tour to minimize the longest distance between consecutive cities
best_tour, total_cost, max_consecutive_dist = find_best_tour(cities)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_dist:.2f}")