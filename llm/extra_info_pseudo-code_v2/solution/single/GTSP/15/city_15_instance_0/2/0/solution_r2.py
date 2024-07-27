import math
from itertools import product

# Coordinates of cities with the depot city being the first entry
cities = [
    (9, 93),  # Depot
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

# Groups of city indices, excluding the depot city
groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]         # Group 2
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two 2D points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_tour_cost(tour):
    """Compute the total travel cost of the tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_shortest_tour():
    # Generate all possible selection of one city from each group
    best_tour = None
    best_cost = float('inf')
    
    # Product gives all combinations of one city from each group
    for combination in product(*groups):
        # Remember to include the depot at the beginning and the end
        complete_tour = [0] + list(combination) + [0]
        
        # Compute the cost of the complete tour
        cost = compute_tour_cost(complete_tour)
        
        # Update the best tour and cost if the current one is better
        if cost < best_cost:
            best_cost = cost
            best_tour = complete_tour
    
    return best_tour, best_cost

# Execute the function to find the shortest tour
shortest_tour, total_travel_cost = find_shortest_tour()

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", round(total_travel_cost, 2))