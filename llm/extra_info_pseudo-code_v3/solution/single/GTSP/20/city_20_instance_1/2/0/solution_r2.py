import math
from itertools import product

# Coordinates of the cities
cities = {
    0: (14, 77),  # Depot
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Brute-force search to find the shortest tour visiting one city from each group
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of exactly one city per group
    for combination in product(*groups):
        # Always start and end at the depot (city 0)
        tour = [0] + list(combination) + [0]
        
        # Calculate the travel cost of this tour
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Check if this tour is better than what we previously found
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

    return best_tour, min_distance

# Execute the function to find the optimal tour
optimal_tour, total_cost = find_shortest_tour()

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")