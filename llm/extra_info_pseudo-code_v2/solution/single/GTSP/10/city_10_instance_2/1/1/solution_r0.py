import math
import itertools

# City coordinates
cities = {
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

# Groups of cities with at least one must visit from each group
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(tour):
    """Calculate the total distance of the given tour."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

def find_shortest_tour():
    """Find the shortest tour visiting exactly one city from each group, starting and ending at depot."""
    min_tour = None
    min_cost = float('inf')
    
    # Generating all combinations of cities from each group
    for combination in itertools.product(*groups):
        # Checking all permutations of each combination
        for perm in itertools.permutations(combination):
            current_tour = [0] + list(perm) + [0]
            current_cost = calculate_total_distance(current_tour)
            if current_cost < min_cost:
                min_cost = current_cost
                min_tour = current_tour
                
    return min_tour, min_cost

# Execute the function to find the shortest tour
tour, cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)