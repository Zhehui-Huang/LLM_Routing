import math
from itertools import permutations

# City coordinates
coordinates = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour):
    """Calculate total tour cost given a list of city indices in the tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

def find_shortest_tour(groups, coordinates):
    """Generate all permutations of the potential city sets and evaluate them."""
    best_tour = None
    best_cost = float('inf')
    
    # Generate possible selections of cities from each group
    from itertools import product
    all_combinations = list(product(*groups))
    
    # Evaluate each combination
    for cities in all_combinations:
        possible_tour = [0] + list(cities) + [0]
        permutations_of_tour = permutations(possible_tour[1:-1])  # All perms of the middle section
        for perm in permutations_of_tour:
            current_tour = [0] + list(perm) + [0]
            current_cost = total_tour_cost(current_tour)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour
    
    return best_tour, best_cost

# Calculate the shortest tour and total cost
shortest_tour, shortest_tour_cost = find_shortest_tour(groups, coordinates)

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", shortest_tour_cost)