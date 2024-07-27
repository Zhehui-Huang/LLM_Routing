import numpy as np
from itertools import product

# Define the coordinates of cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate all the routes through potential combinations
def calculate_best_route():
    best_route = None
    min_cost = float('inf')
    all_possible_routes = product(*city_groups)
    
    # Check every combination of cities (one from each group)
    for route in all_possible_routes:
        # Build full route starting and ending at the depot city
        full_route = [0] + list(route) + [0]
        total_distance = 0
        
        # Calculate total distance of this route
        for i in range(len(full_route) - 1):
            total_distance += euclidean_distance(full_route[i], full_route[i+1])
        
        # Update if the found tour has a lower cost than the current best
        if total_distance < min_cost:
            min_cost = total_distance
            best_route = full_route
    
    return best_route, min_cost

# Finding best tour and its cost
best_tour, cost = calculate_best_route()

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {cost:.2f}")