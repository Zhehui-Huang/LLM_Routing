import itertools
import math

# Cities coordinates, including the depot city 0
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combination tours
def get_possible_tours():
    all_combinations = itertools.product(*groups)
    minimum_cost = float('inf')
    best_tour = None
    
    # Compute and compare tours
    for combination in all_combinations:
        current_tour = [0] + list(combination) + [0]
        current_cost = 0
        
        for i in range(len(current_tour) - 1):
            current_cost += euclidean_distance(current_tobe_odorist[i], current_tour[i+1])
        
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_tour = current_tour
    
    return best_tour, minimum_cost

# Find the shortest tour
shortest_tour, total_cost = get_possible_tours()

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost:.2f}")