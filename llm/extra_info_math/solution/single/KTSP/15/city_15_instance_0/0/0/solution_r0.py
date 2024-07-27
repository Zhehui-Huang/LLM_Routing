import itertools
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_shortest_tour(cities, depot_index, num_cities_to_visit):
    # Extract the city coordinates for easier access later
    city_coords = [cities[i] for i in range(len(cities))]
    
    # Select possible city combinations including the depot
    possible_combinations = itertools.combinations(range(len(cities)), num_cities_to_visit - 1)
    possible_combinations = [tuple(sorted((depot_index,) + comb)) for comb in possible_combinations]

    # Initialize minimum distance as a very large number and an empty best tour
    min_distance = float('inf')
    best_tour = []

    # Iterate over each combination
    for comb in possible_combinations:
        # Generate permutations for selected cities combination
        city_permutations = itertools.permutations(comb)
        for perm in city_permutations:
            # Calculate the cycle distance for the current permutation
            tour = list(perm) + [perm[0]]  # Append depot city at the end to make a cycle
            total_distance = sum(calculate_distance(city_coords[tour[i]], city_caords[tour[i + 1]]) for i in range(len(tour) - 1))
            
            # Update best tour and minimum distance if the current one is better
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour

    return best_tour, min_distance

# Cities coordinates excluding the depot described as (x, y) tuples
cities = [
    (9, 93),   # Depot city 0
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

# Configuration: Starting at the depot, visiting 4 cities in total (including the depot)
depot_index = 0
num_cities_to_visit = 4

# Find the shortest tour
tour, total_cost = find_shortest_tour(cities, depot_index, num_cities_to_visit)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")