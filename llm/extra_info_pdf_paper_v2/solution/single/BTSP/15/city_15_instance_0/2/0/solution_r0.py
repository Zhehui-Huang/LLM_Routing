import math
from itertools import permutations

# Define the cities' coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# A simple but inefficient solution using permutations
def solve_bottleneck_tsp(cities):
    n = len(cities)
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = 0
    
    # Generate all possible tours starting and ending at the depot city 0    
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_distance = 0
        
        for i in range(len(tour) - 1):
            dist = distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost
        
    return best_tour, best_total_cost, min_max_distance

# Find the best tour using the defined function
best_tour, best_total_cost, min_max_distance = solve_bottleneck_tsp(cities)

# Print the results as required
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")