import math
from itertools import combinations

# Define coordinates of each city including the depot city
cities_coordinates = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

def calculate_distance(city_a, city_b):
    xa, ya = cities_coordinates[city_a]
    xb, yb = cities = cities_coordinates[city_b]
    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

# Pre-compute all distances between every pair of cities
distances = {}
for i in cities_coordinates:
    for j in cities_coordinates:
        distances[(i, j)] = calculate_distance(i, j)

# Find the shortest path visiting 4 cities including the depot (city 0)
def find_shortest_tour():
    best_distance = float('inf')
    best_tour = None
    
    # Iterate over combinations of 3 cities (excluding the depot city)
    for cities in combinations(range(1, 20), 3):
        cities_with_depot = (0,) + cities + (0,)  # start and end at the depot
        permutations = itertools.permutations(cities_with_depot)
        
        for perm in permutations:
            tour_distance = sum(distances[(perm[i], perm[i+1])] for i in range(len(perm) - 1))
            
            if tour_distance < best_distance:
                best_distance = tour_distance
                best_tour = perm
                
    return best_tour, best_distance

# Execute the heuristic search
optimal_tour, optimal_distance = find_shortest_tour()

# Output the results
print(f'Tour: {list(optimal_tour)}')
print(f'Total travel cost: {optimal_distance}')