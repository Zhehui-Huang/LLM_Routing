import itertools
import math

# Define the coordinates for each city
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Euclidean distance calculation function
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Calculate all possible routes excluding city 0 (Depot)
routes = list(itertools.permutations(range(1, len(cities))))

min_tour = None
min_max_distance = float('inf')
min_total_cost = float('inf')

# Iterate through each route
for route in routes:
    # Insert the starting depot city and ending depot city (city 0)
    full_route = (0,) + route + (0,)
    
    # Calculate total distance and maximum edge length
    total_distance = 0
    max_distance = 0
    for i in range(len(full_route) - 1):
        dist = euclidean_distance(full_route[i], full_route[i + 1])
        total_distance += dist
        max_distance = max(max_distance, dist)
    
    # Update the minimum maximum distance
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        min_tour = full_route
        min_total_cost = total_distanc

# Output
print(f"Tour: {list(min_tour)}")
print(f"Total travel cost: {min_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_theoretical:.2f}")