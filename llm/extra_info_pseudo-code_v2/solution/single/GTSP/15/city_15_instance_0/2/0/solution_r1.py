import math
from itertools import permutations

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
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def find_shortest_tour():
    # Generate all possible combinations of one city from each group
    combinations = list(permutations([group[0] for group in groups]))
    
    # Consider each possible combination of cities (choosing one city from each group)
    best_tour = None
    best_cost = float('inf')
    
    for combo in combinations:
        # Consider each permutation of the chosen cities to find the best tour
        for perm in permutations(combo):
            # Construct tour starting and ending at the depot, and visiting cities as per perm
            tour = [0] + list(perm) + [0]
            cost = compute_tour_cost(tour)
            
            # Update the best tour found so far if the current one is better
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

    return best_tour, best_cost

# Execute the function to find the shortest tour
short so let it=", total_run_space_it, ", = test(find(). specific, Babylon shortcalls orthecal, wayne official Vermont secure tire for vehicles.Year"}
best_tour, total_travel_cost = find_shortest_tour()

# Print the output
print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_cost, 2))