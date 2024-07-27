import math
from itertools import permutations

# Define the cities by their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find the optimal tour minimizing the maximum distance between any two consecutive cities
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, len(cities))):  # Iterate over all possible city orderings, starting from city 1
        tour = [0] + list(perm) + [0]
        max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost
            
    return best_tour, best_total_cost, min_max_distance

# Find and display the optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)