import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = [
    (84, 67), # Depot city 0
    (74, 40), # City 1
    (71, 13), # City 2
    (74, 82), # City 3
    (97, 28), # City 4
    (0, 31),  # City 5
    (8, 62),  # City 6
    (74, 56), # City 7
    (85, 71), # City 8
    (6, 76),  # City 9
]

# Groups of cities
city_groups = [
    [7, 9], # Group 0
    [1, 3], # Group 1
    [4, 6], # Group 2
    [8],    # Group 3
    [5],    # Group 4
    [2],    # Group 5
]

# Evaluate a given tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Generate all possible tours
def generate_possible_tours():
    # Create permutations of one city from each group
    from itertools import product
    choices = product(*city_groups)
    
    # Add depot at the start and end, calculate cost for each tour
    all_tours = []
    for choice in choices:
        tour = [0] + list(choice) + [0]
        cost = evaluate_tour(tour)
        all_tours.append((tour, cost))
    
    return all_tours

# Use a simple heuristic (trial and checks) to find the minimal tour
def find_minimal_tour():
    all_tours = generate_possible_tours()
    min_tour = min(all_tours, key=lambda t: t[1])
    return min_tour

# Obtain the minimal tour
minimal_tour, minimal_cost = find_minimal_tour()

# Output tour and total travel cost
output = {
    "Tour": minimal_tour,
    "Total travel cost": minimal_cost
}
output