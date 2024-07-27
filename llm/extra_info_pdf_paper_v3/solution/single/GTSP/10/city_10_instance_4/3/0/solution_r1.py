import math
from itertools import permutations

# City coordinates (City index: (x, y))
city_coords = [
    (79, 15),  # Depot
    (79, 55),  # Group 0
    (4, 80),   # Group 1
    (65, 26),  # Group 6
    (92, 9),   # Group 0
    (83, 61),  # Group 3
    (22, 21),  # Group 1
    (97, 70),  # Group 2
    (20, 99),  # Group 5
    (66, 62)   # Group 4
]

# City groups declaration
city_groups = [
    [1, 4],    # Group 0
    [2, 6],    # Group 1
    [7],       # Group 2
    [5],       # Group 3
    [9],       # Group 4
    [8],       # Group 5
    [3]        # Group 6
]

# Euclidean distance calculation function
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate all combinations of cities, one city from each group
def get_all_combinations():
    groups_product = list(permutations([group[0] for group in city_groups]))  # Opt for the first city from each group (simplification)
    return groups_product

# Compute the total cost of a given tour (list of city indices)
def compute_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return total_cost

# Find the shortest tour that visits exactly one city from each group
def find_shortest_path():
    all_combinations = get_all_combinations()
    best_tour = None
    best_cost = float('inf')
    
    for combination in all_combinations:
        tour = [0] + list(combination) + [0]
        cost = compute_total_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    
    return best_tour, best_cost

# Execute the function to get the shortest path
best_tour, best_cost = find_shortest_path()

# Display the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))