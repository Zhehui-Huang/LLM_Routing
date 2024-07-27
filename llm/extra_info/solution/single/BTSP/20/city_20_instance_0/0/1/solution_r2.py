import math
from itertools import permutations

# Define cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Optimize tour to minimize the maximum distance between consecutive cities
def optimize_tour():
    best_tour = None
    best_max_dist = float('inf')
    best_total_cost = float('inf')

    # Generate all permutations excluding the starting city
    for perm in permutations(cities.keys() - {0}):
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_dist = 0
        
        # Calculate total travel cost and maximum distance between consecutive cities
        for i in range(len(tour) - 1):
            dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        
        if max_dist < best_max_dist:
            best_max_dist = max_dist
            best_tour = tour
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, best_max_dist

# Execute the optimization
best_tour, best_cost, max_distance = optimize_tour()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)
print("Maximum distance between consecutive cities:", max_distance)