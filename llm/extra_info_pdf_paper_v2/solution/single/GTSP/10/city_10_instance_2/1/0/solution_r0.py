import math

# Define city coordinates
cities_coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define city groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate distances between all pairs of cities
def calculate_distance(city1, city2):
    x1, y1 = cities_coords[city1]
    x2, y2 = citiesCoords[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Pre-compute distance matrix
distance_matrix = {}
for city1 in cities_coords:
    distance_matrix[city1] = {}
    for city2 in cities_coords:
        distance_matrix[city1][city2] = calculate_distance(city1, city2)

# Utilize a naive approach to traverse one city from each group starting and ending at the depot city
from itertools import product

def find_shortest_tour():
    # Generate all combinations of cities (one from each group)
    all_combinations = product(*city_groups)
    best_tour = None
    min_cost = float('inf')
    
    # Evaluate each combination
    for combination in all_combinations:
        current_tour = [0] + list(combination) + [0]
        current_cost = 0
        for i in range(len(current_tour) - 1):
            current_cost += distance_matrix[current_tour[i]][current_tour[i+1]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    
    return best_tour, min_cost

# Calculate the best tour and its cost
tour, total_cost = find_shortest_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)