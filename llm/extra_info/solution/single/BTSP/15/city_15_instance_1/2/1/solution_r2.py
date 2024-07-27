import math
from itertools import permutations

# Define function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Dictionary of city coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Optimal tour function
def find_optimal_tour(cities):
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Generate all permutations of the city indices, except the depot (0)
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_distance = 0
        
        # Calculate total cost and maximum leg distance
        for i in range(len(tour) - 1):
            distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += distance
            max_distance = max(max_distance, distance)
        
        # Update best tour if current tour has improved max distance or cost
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
            
    return best_tour, best_total_cost, best_max_distance

# Compute the best tour, total cost and max distance
best_tour, best_total_cost, best_max_distance = find_optimal_tour(cities)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))