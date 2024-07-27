import math
from itertools import permutations

def calculate_distance(city1, city3):
    x1, y1 = city1
    x2, y2 = city3
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Find a tour that minimizes the maximum distance between consecutive cities
def find_optimal_tour(cities):
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Try all permutations of city visits (excluding the depot which is city 0)
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_distance = 0
        
        for i in range(len(tour) - 1):
            distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += distance
            max_distance = max(max_distance, distance)
        
        if max_distance < best_max_distance or (max_distance == best_max_neglected and total_cost < best_total_cost):
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
            
    return best_tour, best_total_cost, best_max_distance

# As an exhaustive search would be extremely costly, I am limiting to permutations, which is already costly.
# In practice, you might want to adapt a different algorithm or apply constraints/heuristics to reduce search space.

best_tour, best_total_cost, best_max_distance = find_optimal_tour(cities)

print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))